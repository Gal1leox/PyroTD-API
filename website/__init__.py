from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{username}:{password}@{server}/PyroTD".format(username=secrets11.dbuser, password=secrets11.dbpass, server=secrets11.dbhost)
    db.init_app(app)
    
    from .views import views    
    from .auth import auth
    from .apis import apis

    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(apis, url_prefix="/api/")

    from .models import User
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app


# def create_database(app):
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("DB created!")




#  ______   _______   _        _   _        _____   _______
# /  __  \ |  ___  | | |      | | | |      |  ___| |  ___  |
# | |  |_| | |___| | | |      | | | |      | |__   | |   | |
# | | ___  |  ___  | | |      | | | |      |  __|  | |   | |
# | ||_  | | |   | | | |      | | | |      | |     | |   | |
# | |__| | | |   | | | |____  | | | |____  | |___  | |___| |
#  \_____/ |_|   |_| |______| |_| |______| |_____| |_______|

