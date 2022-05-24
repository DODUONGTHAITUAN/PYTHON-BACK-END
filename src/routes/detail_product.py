from flask import Blueprint, jsonify, request, json
from src.ultils.constants import methods, path

from src.controllers.detail_product import (
    create_detail_product_controller,
    delete_detail_product_controller,
    get_detail_product_by_id_controller,
    update_detail_product_controller,
    create_or_update_detail_product_controller,
)

detail_product = Blueprint("detail_product", __name__)

"""Create new detailproduct"""


@detail_product.route("/create", methods=["POST", "GET"])
def create_detail_product():
    if request.method == "GET":
        return jsonify({"code": 200, "message": " OK"})
    """Get data from request client side"""
    if request.method == "POST":
        data = json.loads(request.data, strict=False)
        return create_detail_product_controller(data)


"""Delete detail_product [DELETE]"""


@detail_product.route("/delete", methods=["DELETE"])
def delete_detail_product():
    try:
        detail_productID = request.args.get("id")
        return delete_detail_product_controller(detail_productID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


"""Get detail_product by id  [GET]"""


@detail_product.route("/get-by-id", methods=["GET"])
def get_detail_product_by_id():
    try:
        detail_productID = request.args.get("id")
        return get_detail_product_by_id_controller(detail_productID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


"""Update detail_product by id  [GET]"""


@detail_product.route("/update", methods=["PUT"])
def update_detail_product():
    try:
        data = request.get_json()
        return update_detail_product_controller(data)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


""" CREATE OR UPDATE """


@detail_product.route("/create-or-update", methods=["POST"])
def create_or_update_detail_product():
    try:
        data = request.get_json()
        print(data)
        return create_or_update_detail_product_controller(data)
    except:
        return jsonify({"code": 4, "message": "Error from server"})
