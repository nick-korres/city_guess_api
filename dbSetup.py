from app import db
import os


def Setup():
    db.drop_all()
    db.create_all()
    db.session.commit()
    file_name = os.listdir(os.path.dirname(__file__)+'/static/images/')
    # print('file name: '+str(file_name))
    for file in file_name:
        city_name = (file.replace('.jpg', '')).replace('_', ' ')
        city = Cities(name=city_name, url='http://127.0.0.1:5000/static/images/'+file) # noqa
        if db.session.query(Cities).filter(Cities.name == city_name).count() == 0: # noqa
            db.session.add(city)

    db.session.commit()
