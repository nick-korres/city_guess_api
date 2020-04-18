from os import environ


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("KEY")
    CORS_HEADERS = 'Content-Type'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
