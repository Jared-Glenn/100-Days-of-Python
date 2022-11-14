from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():

    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()

    return render_template("index.html", posts=posts)

@app.route('/post/<number>')
def post(number):

    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    this_post = response.json()[int(number) - 1]

    return render_template("post.html", post=this_post)



if __name__ == "__main__":
    app.run(debug=True)
