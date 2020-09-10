from flask import send_from_directory
from flask_cors import cross_origin
from models import Cities, cities_schema
import os
from flask import Blueprint, Response  
from sqlalchemy import func

images = Blueprint('images', __name__,static_url_path='/static')

@images.route('/')
@cross_origin()
def welcome():
    return "Hello There"

@images.route('/images/<numOfCities>' , methods=['GET'])
@cross_origin()
def get_cities(numOfCities):
    temp = Cities.query.order_by(func.random()).limit(numOfCities).all()
    result = cities_schema.dumps(temp)
    return Response(result, 200)

correct_path = images.static_url_path+'/images/'
correct_path = os.path.abspath(os.path.dirname(__file__))+correct_path
@images.route('/image/<name>', methods=['GET'])
def show_image(name):
    return send_from_directory(correct_path, filename=name)
