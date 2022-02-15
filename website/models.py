from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String(150))
    p1 = db.Column(db.String(150))
    p2 = db.Column(db.String(150))
    p3 = db.Column(db.String(150))
    p4 = db.Column(db.String(150))
    p5 = db.Column(db.String(150))
    p6 = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())