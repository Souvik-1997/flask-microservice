from app.models import MongoDb

class CustomerModel:
    model_db_instance = MongoDb.mongo_db()
    collection = model_db_instance.customers

    @classmethod
    def create_customer(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_customers(cls):
        return cls.collection.find()
