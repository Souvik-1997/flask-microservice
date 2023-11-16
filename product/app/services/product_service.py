from app.models.product_model import ProductModel

class ProductService:
    @classmethod
    def create_product(cls, data):
        return ProductModel.create_product(data)

    @classmethod
    def get_products(cls):
        return ProductModel.get_products()
