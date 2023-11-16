from json import dumps
from flask import Blueprint
from app.services.customer_service import CustomerService
import uuid

customer_blueprint = Blueprint("customer", __name__, url_prefix="/customer")


@customer_blueprint.route("/home")
def home():
    return "Hello World!"


@customer_blueprint.route("/")
def get_customers():
    customers = CustomerService.get_customers()
    customer_list = dumps(list(customers), default=str)
    # customer_list = [
    #     {"id": customer["id"], "name": customer["name"], "email": customer["email"]}
    #     for customer in customers
    # ]

    response_data = {
        "message": "customer list has been fetched successfully.",
        "success": True,
        "result": {"data": customer_list},
    }
    return dumps(response_data)


@customer_blueprint.route("/create", methods=["POST"])
def create_customer():
    try:
        uu_id = str(uuid.uuid4())
        data = {
            "id": uu_id,
            "name": "Tony Stark",
            "email": "stark@gmail.com",
            "cart": [
                {
                    "customerId": uu_id,
                    "product": {"id": "1", "name": "Product 1", "price": "10"},
                }
            ],
        }
        CustomerService.create_customer(data)
    except Exception as e:
        data = {"error": str(e)}

    response_data = {
        "message": "customer created successfully.",
        "success": True,
        "result": {"data": data},
    }
    return dumps(response_data, default=str)
