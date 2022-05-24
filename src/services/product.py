from flask import jsonify
from sqlalchemy import or_

from src.models.product import Product

from src import db


""" Format products """


def format_products(dataRaw):
    products = []
    for item in dataRaw.items:
        product = format_product(item)
        products.append(product)
    return products


# Format product
def format_product(item):
    # print(item.options[0].color_data)
    option = {}
    if len(item.options) > 0:
        option["ram"] = item.options[0].ram
        option["rom"] = item.options[0].rom
        option["price"] = item.options[0].price
        option["image"] = item.options[0].image
        option["color_id"] = item.options[0].colorID
        option["color_value"] = item.options[0].color_data.value

    return {
        "id": item.id,
        "product_name": item.productName,
        "image": item.image,
        "cpu": item.cpu,
        "gpu": item.gpu,
        "product_date": item.productDate,
        "origin": item.origin,
        "brandID": item.brandID,
        "brand_value": item.brand_data.value,
        "option": option,
    }


def get_all_products_service(data):
    try:
        # Get page
        page = data["page"] or "1"
        # get percent page. One page with per_page element
        per_page = data["per_page"] or "10"
        if not page.isdigit() or not per_page.isdigit():
            page = 1
            per_page = 10
        else:
            page = int(page)
            per_page = int(per_page)
        productRaw = Product.query.paginate(
            per_page=per_page, page=page, error_out=True
        )
        """Format data users"""
        products = format_products(productRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "products": products,
                    "per_page": productRaw.per_page,
                    "current_page": productRaw.page,
                    "total_pages": productRaw.pages,
                },
                "code": 0,
                "message": "Get all products success",
            }
        )
    except Exception as e:
        print("error here: ", e)
        return jsonify({"code": 2, "message": "Get all products fail"})


def create_product_service(data):
    try:
        # get data from client
        productName = data["productName"]
        image = data["imageLink"]
        cpu = data["cpu"]
        gpu = data["gpu"]
        productDate = data["productDate"]
        origin = data["origin"]
        brandID = data["brandID"]
        # check if any param is missed
        if (
            not productName
            or not image
            or not cpu
            or not gpu
            or not productDate
            or not origin
            or not brandID
        ):
            return jsonify({"code": 1, "message": "Missing required param"})

        # create a new product
        newProduct = Product(productName, image, cpu, gpu, productDate, origin, brandID)
        db.session.add(newProduct)
        db.session.commit()
        return jsonify({"code": 0, "message": "product has created"})
    except Exception as e:
        print("Create Product Service: ", e)
        return jsonify({"code": 2, "message": "Error from server"})


# def format_one_product(productRaw):

#     option = {}
#     if len(productRaw.options) > 0:
#         option["ram"] = productRaw.options[0].ram
#         option["rom"] = productRaw.options[0].rom
#         option["price"] = productRaw.options[0].price
#         option["image"] = productRaw.options[0].image
#         option["color_id"] = productRaw.options[0].colorID
#         option["color_value"] = productRaw.options[0].color_data.value

#     return {
#         "id": productRaw.id,
#         "productName": productRaw.productName,
#         "image": productRaw.image,
#         "cpu": productRaw.cpu,
#         "gpu": productRaw.gpu,
#         "productDate": productRaw.productDate,
#         "origin": productRaw.origin,
#         "brandID": productRaw.brandID,
#         "brand_value": productRaw.brand_data.value,
#         "createdAt": productRaw.createdAt,
#         "updatedAt": productRaw.updatedAt,
#         "option": option,
#     }


# def format_product(productsRaw):
#     products = []
#     for item in productsRaw.items:
#         item = format_one_product(item)
#         products.append(item)
#     return products


# def get_all_products_service (no_page):
#     try:
#         page = no_page
#         if page:
#             productsRaw = Product.query.paginate(page = page, per_page = 10)
#         else:
#             return jsonify({"code":1, "message": "not found page number"})

#         products = format_product(productsRaw)
#         return jsonify(
#             {
#             "data":{"product":  products,
#                     "current_page" : productsRaw.page,
#                     "per_page": productsRaw.per_page,
#                     "total_page": productsRaw.pages,
#             },
#             "code": 0,
#             "message": "Got all product",
#             }
#         )
#     except Exception as e:
#         print(e)
#         return jsonify({"code": 2, "message": "Error from server"})


def find_product(id=None, product_name=None):
    """get the fisrt product id that you need to delete"""
    try:
        # product = Product.query.filter_by(id=id).first()
        product = Product.query.filter(
            or_(Product.productName == product_name, Product.id == id)
        ).first()
        if not product is None:
            return {"isExist": True, "product": product, "Code": 0}
        else:
            return {"isExist": False, "Code": 0}
    except Exception as e:
        print(e)
        return {"Code": 1, "message": "Some error when get id from database"}


def delete_product_service(productId):
    """Delete one product in database with provided Id"""
    try:
        response = find_product(productId)
        print(response)
        if response["isExist"] and response["Code"] == 0:
            db.session.delete(response["product"])
            db.session.commit()
            return jsonify({"code": 0, "message": "Delete product successfully"})
        return jsonify({"code": 1, "message": "Detete product unsucessfully"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def update_product_service(data):
    try:
        response = find_product(data["id"])
        if response["isExist"] and response["Code"] == 0:
            product = response["product"]
            product.productName = data["productName"]
            product.image = data["image"]
            product.cpu = data["cpu"]
            product.gpu = data["gpu"]
            product.productDate = data["productDate"]
            product.origin = data["origin"]
            product.brandID = data["brandID"]
            product.createdAt = data["createdAt"]
            product.updatedAt = data["updatedAt"]

            # commit changes in db
            db.session.commit()
            return jsonify({"code": 0, "message": "Update product successfully"})
        return jsonify({"code": 1, "message": "Update product unsucessfully"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})


def get_product_by_id_service(productId):
    """Get one product by id"""
    try:
        response = find_product(productId)
        print(response)
        if response["isExist"] and response["Code"] == 0:
            product = format_product(response["product"])
            return jsonify(
                {"data": product, "code": 0, "message": "Get product successfully"}
            )
        return jsonify({"code": 1, "message": "Get product failure"})
    except Exception as e:
        print(e)
        return jsonify({"code": 2, "message": "Error from server"})
