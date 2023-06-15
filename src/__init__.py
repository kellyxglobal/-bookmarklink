from flask import Flask, jsonify
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db


def create_app(test_config=None):


    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),

        )
    else:
        app.config.from_mapping(test_config)
    """
    @app.get("/")
    def index():
        return "Hello world"

    @app.get("/hello")
    def say_hello():
        return {"message": "Hello world"}
    """

    # Creating blueprints for a users and bookmarks blueprint by creating auth.py file in the src folder and importing blueprint
    db.app=app
    db.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks) 
    
    return app