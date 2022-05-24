from flask import Blueprint, request, jsonify

from src.controllers.product import (
    create_product_controller,
    get_all_products_controller,
    delete_product_controller,
    update_product_controller,
    get_product_by_id_controller,
)

product = Blueprint("product", __name__)


@product.route("/get-products")
def get_all_product():
    try:
        data = request.args.to_dict(flat=True)
        return get_all_products_controller(data)
    except Exception as e:
        print(e)
        return "Hello world"


@product.route("/create", methods=["POST", "GET"])
def create_product():
    if request.method == "GET":
        return jsonify({"code": 200, "message": "NOT OK"})
    data = request.get_json()
    return create_product_controller(data)


# @product.route("/get-all-products", methods=["GET"])
# def get_all_products():
#     """get all products with pagination"""
#     try:
#         page = request.args.get("page", 1, type=int)
#         return get_all_products_controller(page)
#     except Exception as e:
#         print(e)
#         return jsonify({"code": 3, "message": "Can't recieve data from client"})


@product.route("/delete", methods=["DELETE"])
def delete_product():
    """delete one product"""
    try:

        productId = request.args.get("id")
        print(productId)
        return delete_product_controller(productId)
    except:
        return jsonify({"code": 3, "message": "Can't recieve data from client"})


@product.route("/update", methods=["PUT"])
def update_product():
    try:
        data = request.get_json()
        return update_product_controller(data)
    except Exception as e:
        print(e)
        return jsonify({"code": 3, "message": "Can't get data from client"})


@product.route("/get-product-by-id", methods=["GET"])
def get_product_by_id():
    """get one product"""
    try:
        productId = request.args.get("id")
        return get_product_by_id_controller(productId)
    except Exception as e:
        print(e)
        return jsonify({"code": 3, "message": "Can't get id from client"})
