from flask import jsonify
from sqlalchemy import func
from sqlalchemy.sql import and_


from src import db
from src.models.order import Order
from src.ultils.order import format_order, format_orders, get_data_json

#  [ POST ] create new order service
def create_new_order_service(data):
    try:
        order = get_data_json(data)

        # Get current id from order table
        current_id = db.session.query(func.max(Order.id)).scalar()
        if current_id is None:
            current_id = 0

        #  Add keys to a order dict
        order["id"] = current_id + 1
        newOrder = Order(**order)
        print(order)

        db.session.add(newOrder)
        db.session.commit()

        # Using and condition
        order_in_db = Order.query.filter(
            and_(Order.id == order["id"], Order.userID == order["userID"])
        ).first()

        return jsonify(
            {
                "code": 0,
                "message": "order has created",
                "order": format_order(order_in_db),
            }
        )
    except Exception as e:
        print("create new order service: ", e)
        return jsonify({"code": 1, "message": "create new order fail"})


# [ GET ] get order by user id service
def get_order_by_user_id_service(data):
    try:
        # Get userid
        userID = data["userID"]

        # Query db
        orders_raw = Order.query.filter_by(userID=userID).all()
        orders = format_orders(orders_raw)
        return jsonify(
            {"code": 0, "message": "Get order by user id success", "orders": orders}
        )

    except Exception as e:
        print("get order by user id service: ", e)
        return jsonify({"code": 1, "message": "Get order by user id fail"})


# [ POST ] verify order of user  service
def verify_order_user(data):
    try:
        # Get data
        userID = data["userID"]
        orderID = data["id"]
        print({"userID": userID, "orderID": orderID})
        return jsonify({"code": 0, "message": "Verify success"})
    except Exception as e:
        print("Verify order service: ", e)
        return jsonify({"code": 1, "message": "Verify order fail"})
