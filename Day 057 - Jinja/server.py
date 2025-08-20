from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

GENDERIZE_ENDPOINT = "https://api.genderize.io/"
AGIFY_ENDPOINT = "https://api.agify.io/"


@app.route("/")
def hello_world():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/d4e1685d96061b452e86"
    response = requests.get(blog_url)
    data = response.json()

    return render_template("blog.html", posts=data)

@app.route("/guess/<name>")
def hello_guess(name):
    params = {"name": name}

    try:
        genderize_res = requests.get(GENDERIZE_ENDPOINT, params=params, timeout=10)
        agify_res = requests.get(AGIFY_ENDPOINT, params=params, timeout=10)
        genderize_res.raise_for_status()
        agify_res.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}", 500

    genderize_data = genderize_res.json()
    age_data = agify_res.json()

    gender = genderize_data.get("gender", "Unknown")
    age = age_data.get("age", "Unknown")

    return render_template(
        "guess.html",
        name=name.title(),
        gender=gender,
        age=age
    )

if __name__ == "__main__":
    app.run()
