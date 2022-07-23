from pickle import TRUE
from flask import Blueprint, redirect, render_template, url_for, request, flash
from . import db
from . models import User, Player
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . functions.player_processing import battlenet_checker

auth = Blueprint("auth", __name__)

#route for login
@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = data = request.form.get("email")
        password = data = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in!', category='sucess')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('password is incorrect', category='error')

        else:
            flash('email doesnt exist', category='error')


    return render_template ("Login.html", user=current_user)

#Route for sign up
#GET new user info
@auth.route("/sign_up", methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        username = data = request.form.get("username")
        email = data = request.form.get("email")
        password1 = data = request.form.get("password1")
        password2 = data = request.form.get("password2")

        #new user validation, email, username,password.
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        btag_check = battlenet_checker(username)

        #for the people that can never remember their email address
        if email_exists:
            flash('This email already exists', category='error')

        # for the people who like to make new accounts....
        elif username_exists:
            flash('Username in use.', category='error')

        # looking for # tag found in functions\player_processing
        elif btag_check:
            flash('This is not a battletag needs #1234.', category='error')

        #for the people who cannot type the same thing twice
        elif password1 != password2:
            flash('password don\'t match', category='error')
        
        #for the people who want 1 letter usernames
        elif len(username) < 2:
            flash('username is too short.', category='error')

        #for the people that want 1 letter passwords
        elif len(password1) < 6:
            flash('Password too short.', category='error')

        #for the people who submit fake email addresses
        elif len(email) < 4:
            flash('Email is invalid.', category='error')

        # we like these people
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created')
            return redirect(url_for('views.home'))

    return render_template ("sign_up.html", user=current_user)

#logout
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect (url_for('views.home'))