from src.services.detail_product import (
    create_detail_product_service,
    delete_detail_product_service,
    get_detail_product_by_id_service,
    update_detail_product_service,
    create_or_update_detail_product_setvice,
)

"""[POST]"""


def create_detail_product_controller(data):
    return create_detail_product_service(data)


"""[DELETE]"""


def delete_detail_product_controller(id):
    return delete_detail_product_service(id)


"""[GET]"""


def get_detail_product_by_id_controller(id):
    return get_detail_product_by_id_service(id)


"""[PUT] Update detail_product"""


def update_detail_product_controller(data):
    return update_detail_product_service(data)

    """CREATE OR UPDATE detail product"""


def create_or_update_detail_product_controller(data):
    return create_or_update_detail_product_setvice(data)
