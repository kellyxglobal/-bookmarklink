from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from flask import Flask, jsonify, redirect
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db, Bookmark
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config

def create_app(test_config=None):


    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"), 
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHMEY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),

            SWAGGER = {
                'title': "Bookmars API",
                 'uiversion': 3
            }

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

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks) 

    Swagger(app, config=swagger_config, template=template)

    #Tracking Which links we have visited or Not
    #Link tracking to know how many time a user who created the link clicked on it.
    @app.get('/<short_url>')
    @swag_from('./docs/short_url.yml')
    def redirect_to_url(short_url): 
        bookmark = Bookmark.query.filter_by(short_url=short_url).first_or_404()

        if bookmark:
            bookmark.visits = bookmark.visits + 1
            db.session.commit()
            return redirect(bookmark.url)

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handler_404(e):
        return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND
    
    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handler_500(e):
        return jsonify({'error': 'Relax, something minor went wrong.'}), HTTP_500_INTERNAL_SERVER_ERROR
    
    
    return app