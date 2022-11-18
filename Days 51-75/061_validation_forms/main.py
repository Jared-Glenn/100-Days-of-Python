from flask import Flask, render_template
from validation import SignIn
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "any-string"

user = {
    "email": "admin@email.com",
    "password": "12345678",
}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignIn()
    if form.validate_on_submit():
        if user["email"] == form.email.data and user["password"] == form.password.data:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)