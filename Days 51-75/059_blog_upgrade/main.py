from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():

    response = requests.get(url="https://api.npoint.io/13ad96c0a8549487f630")
    entries = response.json()

    return render_template("index.html", page="home", entries=entries)

@app.route("/about")
def about():
    return render_template("about.html", page="about")

@app.route("/contact")
def contact():
    return render_template("contact.html", page="contact")

@app.route('/post/<num>')
def post(num):

    response = requests.get(url="https://api.npoint.io/13ad96c0a8549487f630")
    this_entry = response.json()[int(num) - 1]

    return render_template("post.html", page="post", this_entry=this_entry)

if __name__ == "__main__":
    app.run(debug=True)