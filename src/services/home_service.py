from flask import Response, json


def get_all_product_service():
    products = [
        {
            "id": 1,
            "name": "IP12",
        },
        {"id": 2, "name": "SamSung"},
    ]

    return Response(
        json.dumps({"products": products, "status": 200}),
        status=200,
        mimetype="application/json",
    )
