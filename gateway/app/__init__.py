from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes
    from app.controllers.customer_controller import customer_bp
    from app.controllers.product_controller import product_bp

    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)

    return app
