from app.models import MongoDb

class ProductModel:
    model_db_instance = MongoDb.mongo_db()
    collection = model_db_instance.products

    @classmethod
    def create_product(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_products(cls):
        return cls.collection.find()
