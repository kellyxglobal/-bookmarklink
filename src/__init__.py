from flask import Flask
import os

def create_app(test_config=None):


    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),

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

    return app