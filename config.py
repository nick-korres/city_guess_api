

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xc8\xc9i\x0c\x94\xc5\rM\xb6!1\xe0\x15\xbb\xc0'
    CORS_HEADERS = 'Content-Type'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://nick:nick2525@localhost:5432/city_guess'
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
