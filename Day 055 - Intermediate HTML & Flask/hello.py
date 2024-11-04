from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p> This is is a paragraph </p>' \
            '<img src="https://www.purina-arabia.com/sites/default/files/2020-12/Caring%20For%20a%20Newborn%20KittenTEASER.jpg">' \
            '<iframe src="https://giphy.com/embed/dUQakUPAZw1EY" width="480" height="449" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gracias-dUQakUPAZw1EY">via GIPHY</a></p>'


# Decorator to make text bold
def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

# Decorator to make text italic
def make_italic(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

# Decorator to make text underlined
def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "<h1>Bye!</h1>"

@app.route("/username/<name>/<int:number>")
def greet (name, number):
    return f"Hello, {name}. You are {number} years old.!"


##Python Decorator

if __name__ == "__main__":
    app.run(debug=True)
