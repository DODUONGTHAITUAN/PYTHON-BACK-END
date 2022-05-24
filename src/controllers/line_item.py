from src.services.line_item import (
    create_multiple_line_item_service,
    create_new_line_item_service,
    get_line_items_by_order_id_service,
)


# [ POST ] create new line item controller
def create_new_line_item_controller(data):
    return create_new_line_item_service(data)


# [ POST ] create multiple line item controller
def create_multiple_line_item_controller(data):
    return create_multiple_line_item_service(data)


# [ GET ] get all line items by order id controller
def get_line_items_by_order_id_controller(data):
    return get_line_items_by_order_id_service(data)
