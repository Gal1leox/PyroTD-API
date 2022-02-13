import os
import pathlib
import requests


from google.oauth2 import id_token
from multiprocessing import AuthenticationError
from flask import Flask, render_template, url_for, request, redirect, session, abort
from flask_mysqldb import MySQL
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
#import yaml

app = Flask(__name__)
app.secret_key = "mercerjosch@gmail.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#SQL to be added
#db = yaml.load(open('db.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']

# google auth

GOOGLE_CLIENT_ID = "629346764927-iorq7kpppj8l6174tqns5tqrl3ok0ms9.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")


flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
    )

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) #auth required
        else:
            return function()   

    return wrapper

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_url_reponse=request.url)

    if not session["state"] == request.args["state"]:
        abort(500) #state doesnt match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/protected_area")

@app.route('/')
def index ():
    return "index.html <a href='/login'><button>Login</button></a>"

@app.route('/protected_area')
@login_is_required
def protected_area():
    return "protectedindex.html <a href='/logout'><button>logout</button></a>"

@app.route('/home')
def home ():
    return render_template('home.html')


@app.route("/<usr>")
def user (usr):
    return f"<h1>{usr}</h1>"

if __name__ ==  "__main__":
    app.run(debug=True)

