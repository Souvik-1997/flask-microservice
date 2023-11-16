from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes
    from app.controllers.shipping_controller import shipping_bp

    app.register_blueprint(shipping_bp)

    return app
