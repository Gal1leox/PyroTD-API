from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer)
    winner = db.Column(db.Integer)
    p1_id = db.Column(db.Integer)
    p2_id = db.Column(db.Integer)
    p3_id = db.Column(db.Integer)
    p4_id = db.Column(db.Integer)
    p5_id = db.Column(db.Integer)
    p6_id = db.Column(db.Integer)
    p1_mmr = db.Column(db.Integer)
    p2_mmr = db.Column(db.Integer)
    p3_mmr = db.Column(db.Integer)
    p4_mmr = db.Column(db.Integer)
    p5_mmr = db.Column(db.Integer)
    p6_mmr = db.Column(db.Integer)
    t1_mmr = db.Column(db.Integer)
    t2_mmr = db.Column(db.Integer)
    p1_change = db.Column(db.Integer)
    p2_change = db.Column(db.Integer)
    p3_change = db.Column(db.Integer)
    p4_change = db.Column(db.Integer)
    p5_change = db.Column(db.Integer)
    p6_change = db.Column(db.Integer)
    match_date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class get_Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer)
    winner = db.Column(db.Integer)
    p1_id = db.Column(db.Integer)
    p2_id = db.Column(db.Integer)
    p3_id = db.Column(db.Integer)
    p4_id = db.Column(db.Integer)
    p5_id = db.Column(db.Integer)
    p6_id = db.Column(db.Integer)
    p1_mmr = db.Column(db.Integer)
    p2_mmr = db.Column(db.Integer)
    p3_mmr = db.Column(db.Integer)
    p4_mmr = db.Column(db.Integer)
    p5_mmr = db.Column(db.Integer)
    p6_mmr = db.Column(db.Integer)
    match_date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    mmr = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    icon_id = db.Column(db.Integer)
    player_date_created = db.Column(db.DateTime(timezone=True), default=func.now())