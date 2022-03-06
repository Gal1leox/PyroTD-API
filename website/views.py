from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from .models import Player


views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home ():
    return render_template('home.html', user=current_user)

@views.route('/matches')
@login_required
def matches ():
    return render_template('matches.html', user=current_user)

@views.route('/player')
@login_required
def player():
    #username_exists = Player.query.filter_by(username=username).first()
    return render_template('matches.html', user=current_user)