from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, URLField
from wtforms.validators import DataRequired, URL, NumberRange, Optional
import requests
import security

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
this_query = None


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1500), nullable=True)
    img_url = db.Column(db.String(1500), nullable=False)


class MovieData(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # year = IntegerField("Year", validators=[DataRequired(), NumberRange(min=1000, max=3000)])
    # description = TextAreaField("Description", validators=[DataRequired()])
    # rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=1, max=100)])
    # ranking = IntegerField("Ranking", validators=[DataRequired(), NumberRange(min=1, max=100)])
    # review = TextAreaField("Review", validators=[DataRequired()])
    # img_url = URLField("Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit")


class EditRating(FlaskForm):
    rating = IntegerField("Rating (Out of 100)", validators=[Optional()])
    review = TextAreaField("Review", validators=[Optional()])
    ranking = IntegerField("*Manually Assign Ranking", validators=[Optional()])
    title = StringField("*Change Title", validators=[Optional()])
    year = IntegerField("*Change Year", validators=[Optional()])
    description = TextAreaField("*Change Description", validators=[Optional()])
    img_url = URLField("*Change Poster URL", validators=[Optional()])
    submit = SubmitField("Submit")


db.create_all()


@app.route("/")
def home():
    ordered_movies = Movie.query.order_by(Movie.rating).all()
    ordered_movies.reverse()
    for i in range(len(ordered_movies)):
        ordered_movies[i].ranking = i + 1
    db.session.commit()
    all_movies = db.session.query(Movie).order_by(Movie.ranking.desc()).limit(10)
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieData()
    if form.validate_on_submit():
        global this_query
        this_query = form.title.data
        return redirect(url_for("select"))
    else:
        return render_template('add.html', form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditRating()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        if form.title.data:
            movie.title = form.title.data
        if form.year.data:
            movie.year = form.year.data
        if form.description.data:
            movie.description = form.description.data
        if form.rating.data:
            movie.rating = form.rating.data
        if form.ranking.data:
            movie.ranking = form.ranking.data
        if form.review.data:
            movie.review = form.review.data
        if form.img_url.data:
            movie.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/select')
def select():
    parameters = {
        "api_key": security.TMDB_API_KEY,
        "query": this_query
    }

    response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameters)
    movie_candidates = response.json()['results']
    return render_template('select.html', movies=movie_candidates)


@app.route('/get_movie_details', methods=["GET", "POST"])
def get_movie_details():
    id = request.args.get('id')
    title = request.args.get('title')
    year = request.args.get('year')
    description = request.args.get('description')
    poster = request.args.get('poster')
    new_movie = Movie(
        id=id,
        title=title,
        year=year,
        description=description,
        rating=None,
        ranking=None,
        review=None,
        img_url='https://image.tmdb.org/t/p/original/' + poster,
    )
    db.session.add(new_movie)
    db.session.commit()
    form = EditRating()
    return redirect(url_for('edit', id=id, form=form))


if __name__ == '__main__':
    app.run(debug=True)
