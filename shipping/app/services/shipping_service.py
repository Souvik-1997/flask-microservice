from app.models.shipping_model import ShippingModel

class ShippingService:
    @classmethod
    def create_shipping(cls, data):
        return ShippingModel.create_shipping(data)

    @classmethod
    def get_shipping(cls):
        return ShippingModel.get_shipping()
