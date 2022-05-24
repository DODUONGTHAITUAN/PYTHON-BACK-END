from flask import Blueprint, request
from src.ultils.constants import methods, path
from flask_mail import Message
from src import mail

from src.controllers.auth_controller import get_current_user_controller

auth = Blueprint("auth", __name__)


@auth.route(path["LOGIN"], methods=["POST", "GET"])
def login():
    if request.method == methods["GET"]:
        pass
    elif request.method == methods["POST"]:
        data = request.get_json()
    return get_current_user_controller(data)


@auth.route("/register")
def register():
    return "<h1>Hello world Register Page</h1>"


@auth.route("/send-mail")
def send_mail():
    try:
        msg = Message(
            "Hello from the other side!",
            sender="doduongthaituan201102@gmail.com",
            recipients=["mytranchi2508@gmail.com", "doduongthaituan201102@gmail.com"],
        )
        msg.body = "Hello Tran Chi My"
        msg.html = "<h1 style='color: blue'>This is h1 tags</h1>"
        mail.send(msg)
        print("Hello world")
        return "Send mail success"
    except Exception as e:
        print("index: ", e)
        return "Error when send mail"
