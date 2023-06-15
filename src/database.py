from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#creating fileds for users: Creating a user record with fields
class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(80), unique=True, nullable=False)
    email = db.column(db.String(120), unique=True, nullable=False)
    password = db.column(db.Text(), nullable=False)
    created_at = db.column(db.DateTime, default=datetime.now())
    update_at = db.column(db.DateTime, onupdate=datetime.now())
    #Defining a relaionship with boomark record
    bookmarks = db.relationship('Bookmark', backref="users")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'



#Creating fields for bookmarks
class Bookmark(db.Model):
    id = db.column(db.Integer, primary_key=True)
    #Defining a relationship with User record.
    user_id = db.column(db.integer, db.ForeignKey('User.id'))
    body = db.column(db.Text, nullable=True)
    url = db.column(db.Text, nullable=False)
    short_url = db.column(db.String(3), nullable=False)
    visits = db.column(db.Integer, default=0)
    created_at = db.column(db.DateTime, default=datetime.now())
    update_at = db.column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'Bookmark>>> {self.url}'