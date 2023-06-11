
from flask import Flask

app = Flask(__name__)

## Create an end point or a route by using a decorector as seen 

@app.get("/")
def index():
        return "Hello world"
