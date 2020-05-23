from flask import send_from_directory
from flask_cors import cross_origin
from models import Cities, cities_schema
import os
from flask import Blueprint, Response  # , request
from sqlalchemy import func
# from flask import jsonify
# import json
# from app import db
# from operator import itemgetter 


images = Blueprint('images', __name__,static_url_path='/static')

# temp3 = db.session.query(Cities.name).all();  equivalent to expression below
# temp2 = Cities.query.with_entities(Cities.name).all();
# names = list(map(lambda n: n[0],temp2));  # names of all cities


@images.route('/')
@cross_origin()
def welcome():
    return "Hello There"


# @images.route('/allnames/' , methods=['GET'])
# @cross_origin()
# def get_names():
#     return jsonify(names)

@images.route('/images/<numOfCities>' , methods=['GET'])
@cross_origin()
def get_cities(numOfCities):
    temp = Cities.query.order_by(func.random()).limit(numOfCities).all()
    result = cities_schema.dumps(temp)
    # print(type(result))
    return Response(result, 200)

correct_path = images.static_url_path+'/images/'
correct_path = os.path.abspath(os.path.dirname(__file__))+correct_path
@images.route('/image/<name>', methods=['GET'])
def show_image(name):
    return send_from_directory(correct_path, filename=name)
