from app import db
from sqlalchemy import func
from app.models import Sale

def analyze_sales():
    total_sales_value = db.session.query(func.sum(Sale.total_sale)).scalar() or 0

    total_products_sold = db.session.query(func.sum(Sale.quantity)).scalar() or 0

    total_sales_count = db.session.query(func.count(Sale.id)).scalar() or 0

    average_ticket = total_sales_value / total_sales_count if total_sales_count else 0

    most_sold_product = (
        db.session.query(Sale.product, func.sum(Sale.quantity))
        .group_by(Sale.product)
        .order_by(func.sum(Sale.quantity).desc())
        .first()
    )
    most_sold_product_name = most_sold_product[0] if most_sold_product else 'N/A'
    most_sold_product_quantity = most_sold_product[1] if most_sold_product else 0

    return {
        'total_sales_value': total_sales_value,
        'total_products_sold': total_products_sold,
        'average_ticket': average_ticket,
        'most_sold_product_name': most_sold_product_name,
        'most_sold_product_quantity': most_sold_product_quantity
    }
