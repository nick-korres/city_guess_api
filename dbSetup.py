from app import db
from models import Cities
import os


def Setup():
    db.drop_all()
    db.create_all()
    db.session.commit()
    file_name = os.listdir(os.path.dirname(__file__)+'/static/images/')
    for file in file_name:
        city_name = (file.replace('.jpg', '')).replace('_', ' ')
        city = Cities(name=city_name, url='image/'+file) # noqa
        if db.session.query(Cities).filter(Cities.name == city_name).count() == 0: # noqa
            db.session.add(city)

    db.session.commit()
