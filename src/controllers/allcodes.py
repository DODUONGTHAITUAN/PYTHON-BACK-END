from src.services.allcodes import get_allcodes_by_type_service

""" Get allcode controller """


def get_allcodes_by_type_controller(type):
    return get_allcodes_by_type_service(type)
