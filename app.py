from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"


@app.route("/tweederoute")
def hello_world1():
    return "<p>Hier komt hele andere functie!</p>"