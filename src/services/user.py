from flask import jsonify
from sqlalchemy import or_
from bcrypt import hashpw, checkpw, gensalt
from os import environ
from flask_mail import Message

from src.models.user import User
from src import db
from src import mail
from src.ultils.common import check_code, hash_code
from src.ultils.user import format_user, format_users

# Find user by email or id
def find_user_by_email_or_id(id=None, email=None):
    try:
        user = User.query.filter(or_(User.email == email, User.id == id)).first()
        if not user is None:
            return {"isExist": True, "user": user, "code": 0}
        else:
            return {"isExist": False, "code": 0}
    except Exception as e:
        print(e)
        return {"isExist": False, "code": 1}


# [  ] send mail for client
def send_mail_code_service(data):
    try:
        email = data["email"]
        user_in_db = find_user_by_email_or_id(email=email)
        # Check user exist in db
        if user_in_db["code"] == 0:
            if user_in_db["isExist"]:
                return jsonify({"code": 2, "message": "user had alreadly exist"})
            # Get code
            code = hash_code(email).decode("utf-8")

            # Get sender
            sender = environ.get("MAIL_USERNAME")

            # Create msg
            msg = Message(
                "Verify account",
                sender=sender,
                recipients=[email],
            )
            msg.html = f"""
            <div>
                <span>Your code:</span> 
                <span style='color: red; font-size:20px;'>{code}</span>
            </div> 
            
            """

            # Start send mail
            mail.send(msg)
            return jsonify({"code": 0, "message": "Send code success"})
        return jsonify({"code": 1, "message": "send code failure"})
    except Exception as e:
        print("Send mail: ", e)
        return jsonify({"code": 1, "message": "send code failure"})


# [ POST ] create new user
def create_user_service(data):
    try:
        is_verify = "verify" in data.keys()
        """Get Data"""
        fullName = data["fullName"]
        email = data["email"]
        address = data["address"]
        phonenumber = data["phonenumber"]
        password = data["password"]
        genderID = data["genderID"]
        roleID = data["roleID"]
        verify = data["verify"] if is_verify else -1
        """Verify"""
        if (
            not fullName
            or not email
            or not phonenumber
            or not password
            or not genderID
            or not roleID
            or not verify
        ):
            return jsonify({"code": 1, "message": "Missing required params"})

        user_in_db = find_user_by_email_or_id(email=email)
        # Check user exist in db
        if user_in_db["isExist"] and user_in_db["code"] == 0:
            return jsonify({"code": 2, "message": "user had alreadly exist"})

        if is_verify:
            if check_code(email, verify.encode("utf-8")):

                # Hash password
                hashed = hashpw(password.encode("utf-8"), gensalt())

                """ Create new User"""
                newUser = User(
                    fullName, genderID, address, phonenumber, email, hashed, roleID
                )

                # Insert new user
                db.session.add(newUser)
                db.session.commit()
                return jsonify({"code": 0, "message": "user has created"})
            else:
                return jsonify({"code": 3, "message": "verify code invalid"})
        else:
            # Hash password
            hashed = hashpw(password.encode("utf-8"), gensalt())

            """ Create new User"""
            newUser = User(
                fullName, genderID, address, phonenumber, email, hashed, roleID
            )

            # Insert new user
            db.session.add(newUser)
            db.session.commit()
            return jsonify({"code": 0, "message": "user has created"})
    except Exception as e:
        print("create user", e)
        return jsonify({"code": 4, "message": "Error from server"})


# Get all users and using pagenation
def get_all_users_servive(data):
    try:
        page = data["page"] or "1"
        per_page = data["per_page"] or "10"
        """Check digit"""
        if not page.isdigit() or not per_page.isdigit():
            page = 1
            per_page = 10
        else:
            page = int(page)
            per_page = int(per_page)
        usersRaw = User.query.paginate(per_page=per_page, page=page, error_out=True)
        """Format data users"""
        users = format_users(usersRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "users": users,
                    "per_page": usersRaw.per_page,
                    "current_page": usersRaw.page,
                    "total_pages": usersRaw.pages,
                },
                "code": 0,
                "message": "Get all users success",
            }
        )
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Get all users fail"})


# Delete user in db
def delete_user_service(userId):
    try:
        """Check is digit"""
        response = find_user_by_email_or_id(id=userId)
        if response["isExist"] and response["code"] == 0:
            db.session.delete(response["user"])
            db.session.commit()
            return jsonify({"code": 0, "message": "Delete user success"})
        return jsonify({"code": 1, "message": "Delete user failure"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


# Update user exist in db
def update_user_service(data):
    try:
        response = find_user_by_email_or_id(id=data["id"])
        if response["isExist"] and response["code"] == 0:
            user = response["user"]
            user.fullName = data["fullName"]
            user.address = data["address"]
            user.phonenumber = data["phonenumber"]
            user.email = data["email"]
            user.roleID = data["roleID"]

            # Confirm update row
            db.session.commit()
            return jsonify({"code": 0, "message": "Update user success"})
        return jsonify({"code": 1, "message": "Update user fail"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


# Change password user exist in db
def update_password_user(data):
    try:
        id = data["id"]
        password = data["password"]
        newPassword = data["newPassword"]
        response = find_user_by_email_or_id(id=id)
        if response["isexist"] and response["code"] == 0:
            if check_code(password, response["user"].password):
                """Hash password"""
                hashed = hashpw(password.encode("utf-8"), gensalt())
                response["user"].password = hashed
                db.session.commit()
                return jsonify({"code": 0, "message": "Change password success"})
            return jsonify({"code": 1, "message": "Password invalid"})
        return jsonify({"code": 2, "message": "User invalid"})
    except Exception as e:
        print(e)
        return jsonify({"code": 3, "message": "Error from server"})


# Get user by id
def get_user_by_id_service(id):
    try:
        """Find user"""
        response = find_user_by_email_or_id(id)
        if response["isExist"] and response["code"] == 0:

            # Format user
            user = format_user(response["user"])
            return jsonify({"code": 0, "user": user, "message": "Get user success"})
        return jsonify({"code": 1, "message": "Id invalid"})
    except Exception as e:
        print("service", e)
        return jsonify({"code": 2, "message": "Error from server"})


# get user by email
def get_user_by_email_service(data):
    try:
        email = data["email"]
        password = data["password"]
        print(email, password)
        """Find user"""
        response = find_user_by_email_or_id(email=email)

        # Check email
        if response["isExist"] and response["code"] == 0:

            # Check password
            is_pasword_valid = check_code(
                password, response["user"].password.encode("utf-8")
            )

            if is_pasword_valid:
                user = format_user(response["user"])
                return jsonify({"code": 0, "user": user, "message": "Get user success"})

            return jsonify({"code": 1, "message": "Password invalid"})

        return jsonify({"code": 2, "message": "Email invalid"})
    except Exception as e:
        print("get user by email: ", e)
        return jsonify({"code": 3, "message": "Error from server"})
