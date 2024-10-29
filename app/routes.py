import csv
from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models import Sale

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
