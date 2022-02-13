from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
#import yaml

app = Flask(__name__)

#SQL to be added
#db = yaml.load(open('db.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']


@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/home')
def home ():
    return render_template('home.html')

@app.route('/login', methods=["POST", "GET"])
def login ():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user (usr):
    return f"<h1>{usr}</h1>"

if __name__ ==  "__main__":
    app.run(debug=True)

