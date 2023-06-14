from flask import Blueprint 

#Blueprint for users' authentication
auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

#Tell a user that his data got submitted succesfully
@auth.post('/register')
def register():
    return "User Created"

#Get the current loged in user
@auth.get("/me")
def user():
