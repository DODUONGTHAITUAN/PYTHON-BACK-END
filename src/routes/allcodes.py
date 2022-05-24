from flask import Blueprint, request, jsonify

from src.controllers.allcodes import get_allcodes_by_type_controller

allcodes = Blueprint("allcodes", __name__)


"""[GET] Get allcode by keyMap"""


@allcodes.route("/get-by-type")
def get_allcodes_by_type():
    type = request.args.get("type")
    print(type)
    if type is None:
        return jsonify({"code": 1, "message": "Missing params"})
    return get_allcodes_by_type_controller(type)
