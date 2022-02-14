from flask import Blueprint, redirect, render_template, url_for


auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template ("Login.html")

@auth.route("/sign_up")
def sign_up():
    return render_template ("sign_up.html")

@auth.route("/logout")
def logout():
    return redirect (url_for('views.home'))