def get_current_user_sercice(data):
    username, password = data["username"], data["password"]
    print(username, password)
    return "Hello world"


def handle_create_user_service(data):
    try:
        pass
        return "Hello world create user"
    except:
        print("Hello world")
