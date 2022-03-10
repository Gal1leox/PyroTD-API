from website.__init__ import create_app



application = app = create_app()


if __name__ ==  "__main__":
    app.run(debug=True, port=80)

