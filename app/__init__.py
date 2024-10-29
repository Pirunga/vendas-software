from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Inicializa o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app