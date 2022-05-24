from src.services.option import (
    create_option_service,
    delete_option_service,
    get_all_options_servive,
    delete_option_service,
    get_option_by_id_service,
    update_option_service,
    get_options_by_product_id_service,
    create_or_update_option_service,
)

""" [GET] get options by product id controoler """


def get_options_by_product_id_controller(product_id):
    return get_options_by_product_id_service(product_id)


"""[POST]"""


def create_option_controller(data):
    return create_option_service(data)


"""[GET]"""


def get_all_options_controller(data):
    return get_all_options_servive(data)


"""[DELETE]"""


def delete_option_controller(id):
    return delete_option_service(id)


"""[GET]"""


def get_option_by_id_controller(productID):
    return get_option_by_id_service(productID)


"""[PUT] Update option"""


def update_option_controller(data):
    return update_option_service(data)


def create_or_update_option_controller(data):
    return create_or_update_option_service(data)
