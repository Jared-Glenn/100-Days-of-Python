from flask import Flask, render_template, request
import requests
import smtplib
import security

app = Flask(__name__)

@app.route("/")
def home():

    response = requests.get(url="https://api.npoint.io/13ad96c0a8549487f630")
    entries = response.json()

    return render_template("index.html", page="home", entries=entries, head="reg")


@app.route("/about")
def about():
    return render_template("about.html", page="about", head="reg")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", page="contact", head="reg")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP(security.SMTP_GMAIL) as connection:
            connection.starttls()
            connection.login(user=security.gmail_email1, password=security.gmail_password1)
            connection.sendmail(
                from_addr=security.gmail_email1,
                to_addrs=security.gmail_email2,
                msg= f"Subject:💫 Western Star Message!\n\nFrom: {name}\nEmail: {email}\nPhone:"
                     f" {phone}\n\n{message}".encode('utf-8')
            )
        print(name, email, phone, message)
        return render_template("contact.html", page="contact", head="sent")


@app.route('/post/<num>')
def post(num):

    response = requests.get(url="https://api.npoint.io/13ad96c0a8549487f630")
    this_entry = response.json()[int(num) - 1]

    return render_template("post.html", page="post", this_entry=this_entry, head="reg")


if __name__ == "__main__":
    app.run(debug=True)