from json import dumps
from flask import Blueprint
import requests

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/home")
def home():
    return "Hello World!"


@product_blueprint.route("/", methods=["GET"])
def get_products():
    customer_service_url = "http://127.0.0.1:5002"
    response = requests.get(f"{customer_service_url}/product")
    return response.text, response.status_code


@product_blueprint.route("/create", methods=["POST"])
def create():
    customer_service_url = "http://127.0.0.1:5002"
    response = requests.post(f"{customer_service_url}/product/create")
    return response.text, response.status_code


@product_blueprint.route("/product/<product_id>", methods=["GET"])
def get_product(product_id):
    product_service_url = "http://127.0.0.1:5002"
    response = requests.get(f"{product_service_url}/product/{product_id}")
    return response.text, response.status_code
