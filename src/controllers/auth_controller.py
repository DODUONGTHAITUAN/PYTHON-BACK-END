from src.services.auth_service import get_current_user_sercice


def get_current_user_controller(data):
    return get_current_user_sercice(data)


def handle_create_user_controller(data):
    pass
