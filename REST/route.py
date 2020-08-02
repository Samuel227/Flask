from REST import app, db, jwt, mail
from flask import url_for, jsonify, render_template, request
from .models import User, Planet
from flask_jwt_extended import jwt_required, create_access_token
from flask_mail import Message

"""
@app.cli.comand("db_create")
def db_create():
    db.create_all()
    print("Database Created!")


@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database Destroyed!")


@app.cli.command("db_seed")
def db_seed():
    pass
"""


@app.route("/")
@app.route("/home")
def home():
    return "check it out"


@app.route("/check")
def check():
    return jsonify(message="check and see this")


@app.route("/parameters")
def parameters():
    name = request.args.get("name")
    race = request.args.get("race")


@app.route("/url_variables/<string:name>/<string:race>")
def url_variables(name: str, race: str):
    if race == "black":
        return jsonify(message="black lives matter!!!")
    else:
        return jsonify(message=name + " " + race)


@app.route("/planet", methods=["GET", "POST"])
def planet():
    planet_list = Planet.objects.all()
    return jsonify(data=planet_list)


@app.route("/user", methods=["GET", "POST"])
def user():
    user_list = User.objects.all()
    return jsonify(data=user_list)


@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    # filter by email
    test = User.objects(email=email).first()
    if test:
        return jsonify(message="That email already exists."), 409
    else:
        user_id = request.form["user_id"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(
            user_id=user_id, first_name=first_name, last_name=last_name, email=email
        )
        user.set_password(password)
        user.save()
    return jsonify(message="user created successfully."), 201


@app.route("/login", methods=["POST"])
def login():
    """
    if request.is_json:
        email = request.json["email"]
        password = request.json["password"]
    else:
    """
    email = request.form["email"]
    password = request.form["password"]

    user = User.objects(email=email).first()
    if user and user.get_password(password):
        # access_token = create_access_token(identity=email)
        return jsonify("Login succeeded")
    else:
        return jsonify(message="bad email or password"), 401


@app.route("/retrieve_password/<string:email>", methods=["GET"])
def retrieve_password(email: str):
    user = User.objects(email=email).first()
    if user:
        msg = Message(
            "your planetary API password is " + user.password,
            sender="admin@planetary-api.com",
            recipients=[email],
        )

        mail.send(msg)

        return jsonify(message="Password sent to " + email)

    else:
        return jsonify(message="That email doesn't exist"), 401


@app.route("/planet_details/<int:planet_id>", methods=["GET"])
def planet_details(planet_id: int):
    planet = Planet.objects(planet_id=planet_id).first()
    if planet:
        return jsonify(data=planet)
    else:
        return jsonify(message="Record not found."), 404


@app.route("/add_planet", methods=["POST"])
# @jwt_required  # this will help to secure endpoint
def add_planet():
    # before you post check if the planet_name exist
    planet_id = request.form["planet_id"]
    test = Planet.objects(planet_id=planet_id).first()
    if test:
        return jsonify("There is already a planet by that id"), 409
    else:
        planet_id = request.form["planet_id"]
        planet_name = request.form["planet_name"]
        planet_type = request.form["planet_type"]
        home_star = request.form["home_star"]
        mass = request.form["mass"]
        radius = request.form["radius"]
        distance = request.form["distance"]

        new_planets = Planet(
            planet_id=planet_id,
            planet_type=planet_type,
            home_star=home_star,
            mass=mass,
            radius=radius,
            distance=distance,
        )
        new_planets.save()
        return jsonify(message="data added successfully"), 201


@app.route("/update_planet", methods=["PUT"])
def update_planet():
    planet_id = request.form["planet_id"]
    planet = Planet.objects(planet_id=planet_id).first()
    if planet:
        planet.planet_type = request.form["planet_type"]
        planet.planet_name = request.form["planet_name"]
        planet.home_star = request.form["home_star"]
        mass = request.form["mass"]
        # print(planet.mass)
        radius = request.form["radius"]
        distance = request.form["distance"]
        planet.save()
        return jsonify(message="You updated a planet"), 202
    else:
        return jsonify(message="That planet does not exist"), 404


@app.route("/remove_planet/<int:planet_id>", methods=["DELETE"])
def remove_planet(planet_id: int):
    planet = Planet.objects(planet_id=planet_id).first()
    if planet:
        planet.delete()
        planet.save()
        return jsonify(message="You deleted a planet"), 202
    else:
        return jsonify(message="That planet does not exist"), 404
