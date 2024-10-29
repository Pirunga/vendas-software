from app import db

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    client_name = db.Column(db.String(50), nullable=False)
    product = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_sale = db.Column(db.Float, nullable=False)
