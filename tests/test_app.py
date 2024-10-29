import io
import pytest
from app import create_app, db
from app.models import Sale
from app.utils.analysis import analyze_sales
from datetime import date

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    sale1 = Sale(date=date(2024,9,20), client_id=1, client_name='Julia Santos', product='Impressora', quantity=3, unit_price=600, total_sale=1800)
    sale2 = Sale(date=date(2024,9,13), client_id=2, client_name='João Vieira', product='Notebook', quantity=3, unit_price=3500, total_sale=10500)
    db.session.add(sale1)
    db.session.add(sale2)
    db.session.commit()

def test_upload_csv(client):
    data = {
        'file': (io.BytesIO(b'ID_Venda,Data_Venda,ID_Cliente,Nome_Cliente,Produto,Quantidade,Preco_Unitario,Total_Venda\n1,2024-09-20,105,Julia Santos,Impressora,3,600,1800'), 'sales.csv')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)
    print(response.__dict__)
    assert response.status_code == 200

def test_analyze_sales(init_database):
    analysis = analyze_sales()
    print(analysis)
    assert analysis['total_sales_value'] == 12300
    assert analysis['total_products_sold'] == 6
    assert analysis['average_ticket'] == 6150
    assert analysis['most_sold_product_name'] == 'Notebook'
    assert analysis['most_sold_product_quantity'] == 3

def test_api_get_sales(client, init_database):
    response = client.get('/get_sales?page=1')
    data = response.get_json()
    assert response.status_code == 200
    assert 'sales' in data
    assert len(data['sales']) == 2

def test_generate_daily_report(client, init_database):
    response = client.get('/generate_daily_report')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'
    assert b'%PDF' in response.data[:4]

def test_report_page(client, init_database):
    response = client.get('/report')
    assert response.status_code == 200