from website.__init__ import create_app
import sys
import os
sys.path.append("/opt/python/current/app/MyApp")


application = app = create_app()


if __name__ ==  "__main__":
    app.run(debug=True)

