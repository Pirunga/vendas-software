import io
import pytest
from app import create_app, db
from app.models import Sale
from app.utils.analysis import analyze_sales
from datetime import datetime, date

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
