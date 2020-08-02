from flask import Flask
import os
from config import Config
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(Config)


db = MongoEngine()
db.init_app(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # change this Later
jwt = JWTManager(app)

mail = Mail(app)

# app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
# app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
# app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]

app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
app.config["MAIL_USERNAME"] = "6e88064cae6dc4"
app.config["MAIL_PASSWORD"] = "09075c5558bbc4"


from . import route
