from os import environ

DATABASE_URL = environ.get("DATABASE_URL")
DB_NAME = environ.get("DB_NAME")
URL = DATABASE_URL + "/" + DB_NAME


def config_db(app):
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/demo"
    app.config["SQLALCHEMY_DATABASE_URI"] = URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
