from flask_login import UserMixin
from sqlalchemy import ForeignKey

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, ForeignKey(User.id))
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
