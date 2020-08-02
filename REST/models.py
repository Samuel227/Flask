import flask
from REST import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)


class Planet(db.Document):
    planet_id = db.IntField(unique=True)
    planet_name = db.StringField(max_length=50)
    planet_type = db.StringField(max_length=50)
    home_star = db.StringField(max_length=50)
    mass = db.FloatField()
    radius = db.FloatField()
    distance = db.FloatField()


"""
user = User(
    user_id=21,
    first_name="bkopa",
    last_name="Debora",
    email="bsamuel250@gmail.com",
    password="Samuel229@",
).save()

mercury = Planet(
    planet_id=7,
    planet_name="Mercury",
    planet_type="Class D",
    home_star="Sol",
    mass=3.25823,
    radius=1516,
    distance=35.9836,
).save()

venus = Planet(
    planet_id=8,
    planet_name="Venus",
    planet_type="Class K",
    home_star="Sol",
    mass=4.86724,
    radius=3760,
    distance=67.246,
).save()

"""

