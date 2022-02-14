from flask import Blueprint, redirect, render_template, url_for, request


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    email = data = request.form.get("email")
    password = data = request.form.get("password")
    return render_template ("Login.html")

@auth.route("/sign_up", methods=['GET','POST'])
def sign_up():
    username = data = request.form.get("username")
    email = data = request.form.get("email")
    password1 = data = request.form.get("password1")
    password2 = data = request.form.get("password2")
    return render_template ("sign_up.html")

@auth.route("/logout")
def logout():
    return redirect (url_for('views.home'))