from flask import send_from_directory
from flask_cors import cross_origin
from models import Cities, cities_schema
import os
from flask import Blueprint, Response  # , request

images = Blueprint('images', __name__,static_url_path='/static')


@images.route('/')
@cross_origin()
def welcome():
    return "Hello There"


@images.route('/images/' , methods=['GET'])
@cross_origin()
def get_cities():
    temp = Cities.query.all()
    result = cities_schema.dumps(temp)
    return Response(result, 200)


@images.route('/images/<name>', methods=['GET'])
def show_image(name):
    
    correct_path = images.static_url_path+'/images/'
    correct_path = os.path.abspath(os.path.dirname(__file__))+correct_path
    return send_from_directory(correct_path, filename=name)
