from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'some secret  pass123 '
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:8113@localhost:5000/py_dbase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from py_dbase import models, routes

db.create_all()
