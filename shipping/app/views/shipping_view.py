from json import dumps
from flask import Blueprint
from app.services.shipping_service import ShippingService

shipping_blueprint = Blueprint("shipping", __name__, url_prefix="/shipping")


@shipping_blueprint.route("/home")
def home():
    return "Hello World!"


@shipping_blueprint.route("/")
def get_shipping():
    shipping_details = ShippingService.get_shipping()
    shipping_list = [
        {
            "user_id": shipping["user_id"],
            "product_id": shipping["product_id"],
            "type": shipping["type"],
            "description": shipping["description"],
        }
        for shipping in shipping_details
    ]

    response_data = {
        "message": "Shipping list has been fetched successfully.",
        "success": True,
        "result": {"data": shipping_list},
    }
    return dumps(response_data)


@shipping_blueprint.route("/create", methods=["POST"])
def create_shipping():
    try:
        data = {
            "user_id": "01",
            "product_id": "435355",
            "type": "Road",
            "description": "Shipping by road",
        }
        ShippingService.create_shipping(data)
    except Exception as e:
        data = {"error": str(e)}

    response_data = {
        "message": "Shipping info created successfully.",
        "success": True,
        "result": {"data": data},
    }
    return dumps(response_data, default=str)
