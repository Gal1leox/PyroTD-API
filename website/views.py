from flask import Blueprint, render_template


views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home ():
    return render_template('home.html')

@views.route('/matches')
def matches ():
    return render_template('matches.html')