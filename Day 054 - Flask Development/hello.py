from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def about():
    return "<h1>Bye!</h1>"


##Python Decorator

if __name__ == "__main__":
    app.run()
