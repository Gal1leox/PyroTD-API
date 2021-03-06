from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.__init__ import create_app


application = create_app()


if __name__ ==  "__main__":
    application.debug = True
    application.run()

