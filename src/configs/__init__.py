from flask_cors import CORS, cross_origin
from os import environ

SECRET_KEY = environ.get("SECRET_KEY")


def config_app(app):
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["SECRET_KEY"] = SECRET_KEY
