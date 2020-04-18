from app import db, ma


class Cities(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    url = db.Column(db.String(), unique=True)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<City %r>' % self.name


class CitiesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'url')


cities_schema = CitiesSchema(many=True)
