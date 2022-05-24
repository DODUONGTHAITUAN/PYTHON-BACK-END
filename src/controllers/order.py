from src.services.order import create_new_order_service, get_order_by_user_id_service


# [ POST ] create new order controller
def create_new_order_controller(data):
    return create_new_order_service(data)


# [ GET ] get order by user id controller
def get_order_by_user_id_controller(data):
    return get_order_by_user_id_service(data)
