from flask import Blueprint, jsonify, request
from src.ultils.constants import methods, path

from src.controllers.option import (
    create_option_controller,
    delete_option_controller,
    get_all_options_controller,
    delete_option_controller,
    get_option_by_id_controller,
    get_options_by_product_id_controller,
    update_option_controller,
    create_or_update_option_controller,
)

option = Blueprint("option", __name__)

"""Create new option"""

"""

localhost:8080/option/create
Methods : POST ==> Khi muốn tạo mới dự liêu
GET ==> lay du lieu tư database VD lay het thong tin tuw database
PUT ==> Chinh sua du lieu ==> VD: muon chinh sua thong tin option
DELETE ==> xoa du lieu ==> VD t muon xoa option ==> method delete 
"""


@option.route("/create", methods=["POST", "GET"])
def create_option():
    if request.method == "GET":
        return jsonify({"code": 200, "message": "NOT OK"})
    """Get data from request client side"""
    data = request.get_json()
    return create_option_controller(data)


@option.route("/get-options", methods=["GET"])
def get_all_options():
    try:
        """Convert ImmutableMultiDict to dict"""
        data = request.args.to_dict(flat=True)
        return get_all_options_controller(data)
    except Exception as e:
        print(f"Error at get all option  router: {e}")
        return jsonify({"code": 3, "message": "Error when recieve data from client"})


"""Delete option [DELETE]"""


@option.route("/delete", methods=["DELETE"])
def delete_option():
    try:
        optionID = request.args.get("id")
        print(optionID)
        return delete_option_controller(optionID)
    except:
        return jsonify({"code": 3, "message": "Error get option id"})


"""Get option by id option [GET]"""


@option.route("/get-by-id", methods=["GET"])
def get_option_by_id():
    try:
        productID = request.args.get("productID")
        print(productID)
        return get_option_by_id_controller(productID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


"""Update option by id option [GET]"""


@option.route("/update", methods=["PUT"])
def update_option():
    try:
        data = request.get_json()
        return update_option_controller(data)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


""" [GET] get options by product id """


@option.route("/get-options-by-product-id", methods=["GET"])
def get_options_by_product_id():
    try:
        product_id = request.args.get("productId")
        return get_options_by_product_id_controller(product_id)
    except Exception as e:
        print(e)
        return jsonify({"code": 3, "message": "Error  when get product id"})


# CREATE OR UPDATE
@option.route("/create-or-update", methods=["POST"])
def create_or_update_option():
    try:
        data = request.get_json()
        return create_or_update_option_controller(data)
    except Exception as e:
        print(e)
        return jsonify({"code": 5, "message": "Error when get data option"})
