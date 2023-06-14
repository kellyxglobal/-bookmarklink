from flask import Blueprint 

#Blueprint for users' authentication
auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth.post('/register')
def register():
    return "User Created"