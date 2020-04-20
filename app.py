from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# import config
# import os


app = Flask(__name__, static_url_path='/static')

app.config.from_object('config.DevConfig')

CORS(app)

ma = Marshmallow(app)

db = SQLAlchemy(app)


from routes import images  # To avoid circular imports
app.register_blueprint(images)
from dbSetup import Setup
# Setup()
if __name__ == '__main__':
    app.run()
