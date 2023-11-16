from json import dumps
from flask import Blueprint
from app.services.product_service import ProductService
import uuid

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/home")
def home():
    return "Hello World!"


@product_blueprint.route("/")
def get_products():
    products = ProductService.get_products()
    product_list = dumps(list(products), default=str)
    # product_list = [
    #     {
    #         "id": product["id"],
    #         "name": product["name"],
    #         "description": product["description"],
    #     }
    #     for product in products
    # ]

    response_data = {
        "message": "Product list has been fetched successfully.",
        "success": True,
        "result": {"data": product_list},
    }
    return dumps(response_data)


@product_blueprint.route("/create", methods=["POST"])
def create_product():
    try:
        data = {"id": str(uuid.uuid4()), "name": " Cello Pen", "description": "Awesome pen for student."}
        ProductService.create_product(data)
    except Exception as e:
        data = {"error": str(e)}

    response_data = {
        "message": "Product created successfully.",
        "success": True,
        "result": {"data": data},
    }
    return dumps(response_data, default=str)
