from flask import jsonify
from src.models.allcodes import Allcodes
from src import db


def format_allcodes(data_raw):
    new_codes = []
    for item in data_raw:
        new_item = format_item(item)
        new_codes.append(new_item)
    return new_codes


def format_item(item):
    return {
        "id": item.id,
        "keyMap": item.keyMap,
        "type": item.type,
        "value": item.value,
    }


def get_allcodes_by_type_service(type):
    try:
        data_raw = Allcodes.query.filter_by(type=type).all()
        allcodes_data = format_allcodes(data_raw) if len(data_raw) > 0 else []
        return jsonify(
            {"code": 0, "message": "Get allcodes success", "allcodes": allcodes_data}
        )
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})
