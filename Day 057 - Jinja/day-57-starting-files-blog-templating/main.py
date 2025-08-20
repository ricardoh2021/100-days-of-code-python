from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

POSTS_ENDPOINT = "https://api.npoint.io/f6083ec7ce75b8e7d93f"

def fetch_posts():
    """Helper function to fetch posts from API and wrap them as Post objects"""
    response = requests.get(POSTS_ENDPOINT)
    data = response.json()
    posts = [Post(post.get("id"),
                  post.get("title"),
                  post.get("subtitle"),
                  post.get("body")) for post in data]
    return posts



@app.route('/')
def home():
    data = fetch_posts()

    return render_template("index.html", posts=data)

@app.route("/post/<num>")
def get_post(num):
    print(num)
    posts = fetch_posts()
    # Find the post with matching id
    unique_post = next((p for p in posts if int(p.id) == num), None)

    return render_template("post.html", post=unique_post)


if __name__ == "__main__":
    app.run(debug=True)
