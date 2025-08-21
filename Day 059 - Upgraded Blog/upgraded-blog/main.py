from flask import Flask, render_template
import requests
from Blog import Blog

app = Flask(__name__)


POSTS_ENDPOINT = "https://api.npoint.io/d047e9bb91d5160a2893"

def fetch_posts():
    """Helper function to fetch posts from API and wrap them as Post objects"""
    response = requests.get(POSTS_ENDPOINT)
    data = response.json()
    posts = [
        Blog(
            id=post.get("id"),
            title=post.get("title"),
            subtitle=post.get("subtitle"),
            body=post.get("body"),
            author=post.get("author"),
            date=post.get("date"),
            image_url=post.get("image_url")
        )
        for post in data
    ]
    return posts




@app.route('/')
def home():
    posts = fetch_posts()

    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<num>")
def get_post(num):
    posts = fetch_posts()

    unique_post = next((p for p in posts if int(p.id) == int(num)), None)

    return render_template("post.html", post=unique_post)




if __name__ == "__main__":
    app.run(debug=True)
