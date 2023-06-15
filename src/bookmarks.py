from flask import Blueprint 

#Blueprint for users' authentication
bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

#Tell a user that his bookmark data got submitted succesfully
@bookmarks.get('/')
def get_all():
    return {"bokmarks":[]}