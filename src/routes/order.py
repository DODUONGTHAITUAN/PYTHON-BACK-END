from flask import Blueprint, request, jsonify

from src.controllers.order import (
    create_new_order_controller,
    get_order_by_user_id_controller,
)

order = Blueprint("order", __name__)

# [ POST ] create new order
@order.route("/create", methods=["POST"])
def create_new_order():
    try:
        # Get data from client
        data = request.get_json()

        # return result
        return create_new_order_controller(data)
    except Exception as e:
        print("Create new order router: ", e)
        return jsonify({"code": 1, "message": "Error from server"})


# [ GET ] get order by user id
@order.route("/get-orders-by-user-id", methods=["GET"])
def get_order_by_user_id():
    try:
        data = request.args.to_dict(flat=True)
        return get_order_by_user_id_controller(data)
    except Exception as e:
        print("get order by user id route: ", e)
        return jsonify({"code": 2, "message": "Error from server"})
