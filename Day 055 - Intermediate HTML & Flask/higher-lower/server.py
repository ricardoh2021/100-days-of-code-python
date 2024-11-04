from flask import Flask
import random

app = Flask(__name__)


randomNumber = random.randint(0,9)
print(randomNumber)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            '<iframe src="https://giphy.com/embed/gMTnEFm4U4gV3tK5uL" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/PermissionIO-going-live-in-10-countdown-from-gMTnEFm4U4gV3tK5uL">via GIPHY</a></p>'


# Decorator to style text in yellow
def style_yellow(func):
    def wrapper():
        return f'<h1 style="color: purple;">{func()}</h1>'

    return wrapper


# Decorator to style text in red
def style_red(func):
    def wrapper():
        return f'<h1 style="color: red;">{func()}</h1>'

    return wrapper


# Decorator to style text in green
def style_green(func):
    def wrapper():
        return f'<h1 style="color: green;">{func()}</h1>'

    return wrapper


@app.route("/<int:number>")
def get_number_guessed(number):
    if number < randomNumber:
        @style_yellow
        def message():
            return "Too low"

        return message() + '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    elif number > randomNumber:
        @style_red
        def message():
            return "Too high"

        return message() + '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    else:
        @style_green
        def message():
            return "You Found Me!"

        return message() + '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

##Python Decorator

if __name__ == "__main__":
    app.run(debug=True)
