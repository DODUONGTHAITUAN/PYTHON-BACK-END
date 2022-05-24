from flask import Blueprint, jsonify, request
from src.ultils.constants import methods, path

from src.controllers.user import (
    create_user_controller,
    delete_user_controller,
    get_all_users_controller,
    delete_user_controller,
    get_user_by_email_controller,
    get_user_by_id_controller,
    send_mail_code_controller,
    update_user_controller,
)

user = Blueprint("user", __name__)

"""Create new User"""

"""

localhost:8080/user/create
Methods : POST ==> Khi muốn tạo mới dự liêu
GET ==> lay du lieu tư database VD lay het thong tin tuw database
PUT ==> Chinnhr sua du lieu ==> VD: muon chinh suwar thong tin user
DELETE ==> xoas du lieu ==> VD t muon xoa user ==> method delete 
"""


# [ POST ] create new user
@user.route("/create", methods=["POST", "GET"])
def create_user():
    if request.method == "GET":
        return jsonify({"code": 200, "message": "NOT OK"})
    """Get data from request client side"""
    data = request.get_json()
    return create_user_controller(data)


@user.route("/verify-account", methods=["POST"])
def verify_account():
    try:
        data = request.get_json()
        print(data)
        return send_mail_code_controller(data)
    except Exception as e:
        print(e)
        return jsonify({"code": 1, "message": "send mail failure"})


# Get all users
@user.route("/get-users", methods=["GET"])
def get_all_users():
    try:
        """Convert ImmutableMultiDict to dict"""
        data = request.args.to_dict(flat=True)
        return get_all_users_controller(data)
    except Exception as e:
        print(f"Error at get all user  router: {e}")
        return jsonify({"code": 3, "message": "Error when recieve data from client"})


#  Delete user
@user.route("/delete", methods=["DELETE"])
def delete_user():
    try:
        userID = request.args.get("id")
        return delete_user_controller(userID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


# Get user by id
@user.route("/get-by-id", methods=["GET"])
def get_user_by_id():
    try:
        userID = request.args.get("id")
        return get_user_by_id_controller(userID)
    except:
        return jsonify({"code": 2, "message": "Error from server"})


# Get user by email
@user.route("/get-by-email", methods=["POST"])
def get_user_by_email():
    try:
        data = request.get_json()
        return get_user_by_email_controller(data)
    except:
        return jsonify({"code": 4, "message": "Error when get data from client"})


#  Update user by id
@user.route("/update", methods=["PUT"])
def update_user():
    try:
        data = request.get_json()
        return update_user_controller(data)
    except:
        return jsonify({"code": 2, "message": "Error from server"})
