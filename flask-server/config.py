import os

from .base_config import Config


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

    EMAIL_METHOD = 'SMTP'

    DATABASE_NAME = 'medhack_info_vaccine'
    DATABASE_PASSWORD = 'postgres'
    DATABASE_USER = 'postgres'
    DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')

    ENCRIPTION_KEY = 'c4b1d379cf3906e65fafafb5e525c35e163ead77b9a70455c93bd006f8762169'
    SECRET_KEY = b'_5@3y2XlOp!sT1!'

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

    UI_SECRET_NAME = 'secret_name'
    UI_SECRET_KEY = 'secret_phrase'

    BASE_UI_URL = 'http://127.0.0.1:3000'
    BASE_API_URL = 'http://127.0.0.1:5000'

    RATE_LIMIT_INTERVAL = 1
    RATE_LIMIT_ALLOWED_NUMBER_OF_REQUESTS = 10
    ENV_PREFIX = 'DEV'


config = {
    'development': DevelopmentConfig,
}
