from flask import Flask, render_template, url_for, request, redirect, session, abort
from website import create_app



application = create_app()


if __name__ ==  "__main__":
    application.run(debug=True, port=80)

