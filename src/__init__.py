from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


from .routes import routes
from .configs import config_app
from .configs.configDB import config_db
from .configs.config_mail import config_mail


app = Flask(__name__)
db = SQLAlchemy(app)
mail = Mail()

from .models.allcodes import Allcodes
from .models.user import User
from .models.product import Product
from .models.option import Option
from .models.detail_product import DetailProduct
from .models.line_item import LineItem
from .models.order import Order

def create_app():
    """Config app"""
    config_app(app)

    """Routes app"""
    routes(app)

    """Config database app"""
    config_db(app)
    db.init_app(app)

    """ Config mail """
    config_mail(app=app)
    mail.init_app(app)

    db.create_all()

    return app
