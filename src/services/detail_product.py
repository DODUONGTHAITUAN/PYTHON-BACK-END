from flask import jsonify
from src.models.detail_product import DetailProduct
from src import db

"""[POST]"""


def create_detail_product_service(data):
    try:
        """Get Data"""
        contentHTML = data["contentHTML"]
        contentMarkdown = data["contentMarkdown"]
        simSlots = data["sim_slots"]
        osID = data["osID"] or "BAT1"
        batteryText = data["batteryText"]
        batteryID = data["batteryID"]
        screenID = data["screenID"]
        screenText = data["screenText"]
        brandID = data["brandID"]
        featureID = data["featureID"]
        productID = data["productID"]
        """Verify"""
        if (
            not featureID
            or not simSlots
            or not batteryText
            or not screenText
            or not productID
        ):
            return jsonify({"code": 1, "message": "Missing required params"})
        """Handle data and return result"""

        """ Create new detial_Product"""
        newdetail_Product = DetailProduct(
            contentHTML,
            contentMarkdown,
            simSlots,
            osID,
            batteryText,
            batteryID,
            screenText,
            screenID,
            brandID,
            featureID,
            productID,
        )

        # Insert new user
        db.session.add(newdetail_Product)
        db.session.commit()
        return jsonify({"code": 0, "message": "detail_product has created"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def formart_detail_Products(detail_ProductsRaw):
    detail_Products = []
    for item in detail_ProductsRaw.items:
        Product = format_detail_product(item)
        detail_Products.append(Product)
    return detail_Products


def format_detail_product(detail_productRaw):
    return {
        "id": detail_productRaw.id,
        "productID": detail_productRaw.productID,
        "contentHTML": detail_productRaw.contentHTML,
        "contentMarkdown": detail_productRaw.contentMarkdown,
        "simSlots": detail_productRaw.simSlots,
        "osID": detail_productRaw.osID,
        "batteryText": detail_productRaw.batteryText,
        "batteryID": detail_productRaw.batteryID,
        "screenText": detail_productRaw.screenText,
        "screenID": detail_productRaw.screenID,
        "brandID": detail_productRaw.brandID,
        "featureID": detail_productRaw.featureID,
    }


"""[DELETE]"""


def delete_detail_product_service(detail_productId):
    try:
        """Check is digit"""
        print(detail_productId)
        response = find_detail_product(detail_productId)
        if response["isExist"] and response["code"] == 0:
            db.session.delete(response["detail_product"])
            db.session.commit()
            return jsonify({"code": 0, "message": "Delete detail_product success"})
        return jsonify({"code": 1, "message": "Delete detai_product failure"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


"""Find detail_product"""


def find_detail_product(id):
    try:
        detail_product = DetailProduct.query.filter_by(productID=id).first()
        if not detail_product is None:
            return {"isExist": True, "detail_product": detail_product, "code": 0}
        else:
            return {"isExist": False, "code": 0}
    except Exception as e:
        print(e)
        return {"isExist": False, "code": 1}


"""Update detail_product [PUT]"""


def update_detail_product_service(data):
    try:
        response = find_detail_product(data["productID"])
        if response["isExist"] and response["code"] == 0:
            detail_product = response["detail_product"]
            detail_product.productID = data["productID"]
            detail_product.contentHTML = data["contentHTML"]
            detail_product.contentMarkdown = data["contentMarkdown"]
            detail_product.simSlots = data["sim_slots"]
            detail_product.osID = data["osID"]
            detail_product.batteryText = data["batteryText"]
            detail_product.batteryID = data["batteryID"]
            detail_product.screenText = data["screenText"]
            detail_product.screenID = data["screenID"]
            detail_product.brandID = data["brandID"]
            detail_product.featureID = data["featureID"]
            # Confirm update row
            db.session.commit()
            return jsonify({"code": 0, "message": "Update detail_product success"})
        return jsonify({"code": 1, "message": "Update detail_product fail"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def get_detail_product_by_id_service(detail_productId):
    try:
        """Find detail_product"""
        response = find_detail_product(detail_productId)
        if response["isExist"] and response["code"] == 0:
            print(response["detail_product"].productID)
            detail_product = format_detail_product(response["detail_product"])
            return jsonify(
                {
                    "code": 0,
                    "detail_product": detail_product,
                    "message": "Get detail_product success",
                }
            )
        return jsonify({"code": 1, "message": "Id invalid"})
    except Exception as e:
        print("service", e)
        return jsonify({"code": 2, "message": "Error from server"})


# Create or update
def create_or_update_detail_product_setvice(data):
    response = find_detail_product(data["productID"])
    if response["code"] == 0:
        if response["isExist"]:
            return update_detail_product_service(data)
        elif not response["isExist"]:
            return create_detail_product_service(data)
    else:
        return jsonify({"code": 4, "message": "Error from server"})
