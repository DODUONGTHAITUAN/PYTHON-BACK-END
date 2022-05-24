from flask import jsonify

from src.ultils.line_item import format_line_items, get_data_json
from src.models.line_item import LineItem
from src import db


# [ POST ] create new line item service
def create_new_line_item_service(data):
    try:
        # Create instance line_item
        line_item = get_data_json(data)
        new_line_item = LineItem(**line_item)

        #  Insert recod in database
        db.session.add(new_line_item)
        db.session.commit()

        return jsonify({"code": 0, "message": "Create line item success"})
    except Exception as e:
        print("create new line item service: ", e)
        return jsonify({"code": 1, "message": "Create line item fail"})


# [ POST ] create muliple line item service
def create_multiple_line_item_service(data):
    try:
        print(data)
        line_items = data["data"]
        for item in line_items:
            line_item = get_data_json(item)
            new_line_item = LineItem(**line_item)
            db.session.add(new_line_item)
        db.session.commit()

        return jsonify({"code": 0, "message": "Create line item success"})
    except Exception as e:
        print("create new line item service: ", e)
        return jsonify({"code": 1, "message": "Create line item fail"})


#  [ GET ] get all line_item by order id
def get_line_items_by_order_id_service(data):
    try:
        #  Get order id
        orderID = data["orderID"]
        print(orderID)

        # Query
        line_items_raw = LineItem.query.filter_by(orderID=orderID).all()
        line_items = format_line_items(line_items_raw)

        # Return result
        return jsonify(
            {
                "code": 0,
                "message": "Get line items by order id success",
                "line_items": line_items,
            }
        )
    except Exception as e:
        print("get line items by order id service: ", e)
        return jsonify({"code": 1, "message": "Get line items by order id fail"})
