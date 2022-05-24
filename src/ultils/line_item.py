def get_data_json(data):
    return {
        "orderID": data["orderID"],
        "productID": data["productID"],
        "quantity": data["quantity"],
        "price": data["price"],
    }


def format_line_items(data):
    return [format_line_item(item) for item in data]


def format_line_item(data):
    return {
        "id": data["id"],
        "orderID": data["orderID"],
        "productID": data["productID"],
        "quantity": data["quantity"],
        "price": data["price"],
    }
