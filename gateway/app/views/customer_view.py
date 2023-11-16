from json import dumps
from flask import Blueprint
import requests

customer_blueprint = Blueprint("customer", __name__, url_prefix="/customer")


@customer_blueprint.route("/home")
def home():
    return "Hello World!"


@customer_blueprint.route("/", methods=["GET"])
def get_customers():
    customer_service_url = "http://127.0.0.1:5001"
    response = requests.get(f"{customer_service_url}/customer")
    return response.text, response.status_code


@customer_blueprint.route("/create", methods=["POST"])
def create():
    customer_service_url = "http://127.0.0.1:5001"
    response = requests.post(f"{customer_service_url}/customer/create")
    return response.text, response.status_code


@customer_blueprint.route("/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer_service_url = "http://127.0.0.1:5001"
    response = requests.get(f"{customer_service_url}/customer/{customer_id}")
    return response.text, response.status_code
