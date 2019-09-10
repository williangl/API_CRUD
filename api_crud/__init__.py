"""Start flask app."""
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from .models import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/api_crud_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object('api_crud.config.Development')

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    JWTManager(app)

    from .costumer import bp_costumer
    app.register_blueprint(bp_costumer)

    return app
