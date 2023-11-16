from app.models import MongoDb

class ShippingModel:
    model_db_instance = MongoDb.mongo_db()
    collection = model_db_instance.data

    @classmethod
    def create_shipping(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_shipping(cls):
        return cls.collection.find()
