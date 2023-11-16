from app.models.customer_model import CustomerModel

class CustomerService:
    @classmethod
    def create_customer(cls, data):
        return CustomerModel.create_customer(data)

    @classmethod
    def get_customers(cls):
        return CustomerModel.get_customers()
