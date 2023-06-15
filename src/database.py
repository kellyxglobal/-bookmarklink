from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()

#creating fileds for users: Creating a user record with fields
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    #definng relationship with bookmark
    bookmarks = db.relationship('Bookmark', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'



#Creating fields for bookmarks
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(3), nullable=True)
    visits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    #Look for a way of creating a short_url from a given url
    def generate_short_characters(self):
        #In python -m flask shell, string.digits='0123456789', string.ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        characters = string.digits+string.ascii_letters
        #Choose random 3 letters from characters
        #random.choices(string.ascii_letters, k=3) = ['e', 'T', 'd'] 
        # however, to convert the list output to a string, we use ''.join(random.choices(string.ascii_letters, k=3))
        # output = 'etd' 
        picked_chars = ''.join(random.choices(characters, k=3))

        #Making sure that picked_char does not exist in a db
        link=self.query.filter_by(short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars
        #find a way of getting all the possible characters and 
        # picking randomly all the possible characters an also making sure that the picked ones has not being picked before
        

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    def __repr__(self) -> str:
        return 'Boomark>>> {self.url}'