import os

class Config:
    DEBUG = os.environ.get('DEBUG', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    MONGO_URI = os.getenv("DB_URL", "DB_URL")
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", "FLASK_RUN_PORT")