from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

now = dt.datetime.now()
year = now.strftime("%Y")


@app.route("/")
def main_site():
    return render_template("index.html", year=year)

@app.route("/guess/<chosen_name>")
def guess_site(chosen_name):
    data = {
        "name": chosen_name
    }

    age_response = requests.get(url="https://api.agify.io", params=data)
    age = age_response.json()["age"]
    gender_response = requests.get(url="https://api.genderize.io", params=data)
    gender = gender_response.json()["gender"]

    chosen_name = chosen_name.capitalize()

    return render_template("guess.html", chosen_name=chosen_name, age=age, gender=gender)

@app.route("/blog")
def blog_site():

    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()

    return render_template("blog.html", blog_posts=blog_posts)



if __name__ == "__main__":
    app.run(debug=True)