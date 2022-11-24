from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange, URL
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField
import requests
import smtplib
import security
import datetime

# PREPARE APP
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'anything'
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)


# POSTS MODEL
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Body')
    submit = SubmitField("Submit Post")


db.create_all()


# HOME
@app.route("/")
def home():
    entries = db.session.query(BlogPost).all()

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

    post_selected = BlogPost.query.get(int(num))

    return render_template("post.html", page="post", this_entry=post_selected, head="reg")


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if request.method == "POST":
        now = datetime.datetime.now()
        date_time_string = now.strftime("%B %d, %Y")
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date_time_string,
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("make-post.html", form=form, page=contact, head="reg", page_version="New Post")


@app.route('/edit-post/<num>', methods=["GET", "POST"])
def edit_post(num):
    post = BlogPost.query.get(int(num))
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if request.method == "POST":
        post.title=edit_form.title.data
        post.subtitle=edit_form.subtitle.data
        post.body=edit_form.body.data
        post.author=edit_form.author.data
        post.img_url=edit_form.img_url.data
        db.session.commit()
        return render_template("post.html", page="post", this_entry=post, head="reg")

    return render_template("make-post.html", form=edit_form, page=contact, head="reg", page_version="Edit Post")


@app.route("/delete")
def delete():
    post_id = request.args.get('id')
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug=True)