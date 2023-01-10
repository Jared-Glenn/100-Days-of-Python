from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor


# PREPARE APP
app = Flask(__name__, template_folder='templates')
app.app_context().push()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'anything'
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)


# HOME
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)