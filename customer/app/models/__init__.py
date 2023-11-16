import pymongo
from config import Config


class MongoDb:
    @staticmethod
    def mongo_db():
        try:
            client = pymongo.MongoClient(Config.MONGO_URI)
            client.server_info()
            db = client.customer
            print(" * DB connection established...")

        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(" * Failed to connect DB", err)

        return db
