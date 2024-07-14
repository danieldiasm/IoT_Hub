# Main file of IoT Hub Web Application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the Index!"
