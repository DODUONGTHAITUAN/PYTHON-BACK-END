 
from src.services.product import (create_product_service,  get_all_products_service, 
delete_product_service, update_product_service, get_product_by_id_service)


def create_product_controller(data):
    return create_product_service(data)

def get_all_products_controller(page):
    return get_all_products_service(page)

def delete_product_controller(productId):
    return delete_product_service(productId)

def update_product_controller (data):
    return update_product_service(data)

def get_product_by_id_controller(productId):
    return get_product_by_id_service(productId)

