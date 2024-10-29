import csv
from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify

from app import db
from app.models import Sale
from app.utils.analysis import analyze_sales

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not file.filename.endswith('.csv'):
        flash('Formato inválido. Por favor, envie um arquivo CSV.', 'error')
        return redirect(url_for('main.index'))

    reader = csv.DictReader(file.read().decode('utf-8').splitlines())
    for row in reader:
        sale = Sale(
            date=datetime.strptime(row['Data_Venda'], '%Y-%m-%d').date(),
            client_id=int(row['ID_Cliente']),
            client_name=row['Nome_Cliente'],
            product=row['Produto'],
            quantity=int(row['Quantidade']),
            unit_price=float(row['Preco_Unitario']),
            total_sale=float(row['Total_Venda'])
        )
        db.session.add(sale)
    db.session.commit()
    flash('Arquivo CSV importado com sucesso!', 'success')
    return redirect(url_for('main.index'))

@main.route('/report')
def report():
    sales = Sale.query.all()
    analysis = analyze_sales()
    return render_template('report.html', sales=sales, analysis=analysis)

@main.route('/get_sales', methods=['GET'])
def get_sales():
    page = request.args.get('page', 1, type=int)
    per_page = 20

    sales_paginated = Sale.query.paginate(page=page, per_page=per_page)
    sales_data = [
        {
            'date': sale.date.strftime('%d/%m/%Y'),
            'customer_name': sale.client_name,
            'product': sale.product,
            'quantity': sale.quantity,
            'unit_price': f'{sale.unit_price:.2f}',
            'total_sale': f'{sale.total_sale:.2f}'
        }
        for sale in sales_paginated.items
    ]

    return jsonify({
        'sales': sales_data,
        'has_next': sales_paginated.has_next
    })
