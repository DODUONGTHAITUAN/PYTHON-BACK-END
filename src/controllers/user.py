from src.services.user import (
    create_user_service,
    delete_user_service,
    get_all_users_servive,
    delete_user_service,
    get_user_by_id_service,
    update_user_service,
    get_user_by_email_service,
    send_mail_code_service,
)

# Send mail code services
def send_mail_code_controller(data):
    return send_mail_code_service(data)


# [ POST ] get all user by email
def get_user_by_email_controller(data):
    return get_user_by_email_service(data)


# [ POST ] create user
def create_user_controller(data):
    return create_user_service(data)


# [ GET ] get all users
def get_all_users_controller(data):
    return get_all_users_servive(data)


# [ DELETE ] delete user
def delete_user_controller(id):
    return delete_user_service(id)


#  [ GET ] get user by id
def get_user_by_id_controller(id):
    return get_user_by_id_service(id)


#  [ PUT ] update user by id
def update_user_controller(data):
    return update_user_service(data)
