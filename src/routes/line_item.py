from flask import Blueprint, jsonify, request

from src.controllers.line_item import (
    create_multiple_line_item_controller,
    create_new_line_item_controller,
    get_line_items_by_order_id_controller,
)


line_item = Blueprint("line_item", __name__)

# [ POST ] create new line item
@line_item.route("/create", methods=["POST"])
def create_new_line_item():
    try:
        data = request.get_json()
        return create_new_line_item_controller(data)
    except Exception as e:
        print("create new line item route: ", e)
        return jsonify({"code": 2, "message": "Error from server"})


# [ POST ] create multiple line item
@line_item.route("/create/multiple", methods=["POST"])
def create_multiple_line_item():
    try:
        data = request.get_json()
        return create_multiple_line_item_controller(data)
    except Exception as e:
        print("create new line item route: ", e)
        return jsonify({"code": 2, "message": "Error from server"})


# [ GET ] get all line items by order id
@line_item.route("/get-line-items", methods=["GET"])
def get_line_items_by_order_id():
    try:
        data = request.args.to_dict(flat=True)
        return get_line_items_by_order_id_controller(data)
    except Exception as e:
        print("create new line item route: ", e)
        return jsonify({"code": 2, "message": "Error from server"})
