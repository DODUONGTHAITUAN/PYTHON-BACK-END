from flask import Blueprint, request

from src.controllers.home_controller import get_all_product_controller


home = Blueprint("home", __name__)


@home.route("/")
def index():
    return "<h1>Hello Home Page</h1>"


@home.route("/products", methods=["GET"])
def products():
    return get_all_product_controller()

    # locallhost:://products
