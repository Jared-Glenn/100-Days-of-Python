from flask import Flask, render_template, jsonify, request, redirect, url_for
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL, Regexp
import csv
import datetime


# Create the App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'anything'
# Configure the SQLite Database
engine = create_engine("sqlite:///C:/Users/Jared/Documents/3. Programming/100 Days of Python/Days 76-100/088_adjutant/instances/todo.db", echo=True)

meta = MetaData()
MetaData.reflect(meta, bind=engine)


global_focus = datetime.date.today()


# TO DO MODEL
to_do_items = Table(
    'todo', meta,
    Column('id', Integer, primary_key=True),
    Column('item', String(250), nullable=False),
    Column('date', String(250)),
    extend_existing=True,
)

meta.create_all(engine)

@app.route("/")
def home():
    global global_focus
    focus = global_focus
    day_before = focus - (datetime.timedelta(days=1))
    day_before_str = day_before.strftime("%B %d, %Y")
    db_weekday = day_before.strftime("%A")
    day_after = focus + (datetime.timedelta(days=1))
    day_after_str = day_after.strftime("%B %d, %Y")
    da_weekday = day_after.strftime("%A")
    two_days_after = focus + (datetime.timedelta(days=2))
    two_days_after_str = two_days_after.strftime("%B %d, %Y")
    tda_weekday = two_days_after.strftime("%A")
    focus_str = focus.strftime("%B %d, %Y")
    f_weekday = focus.strftime("%A")
    return render_template("index.html", focus=focus_str, f_weekday=f_weekday, day_before=day_before_str, db_weekday=db_weekday,
                           day_after=day_after_str, da_weekday=da_weekday, two_days_after=two_days_after_str,
                           tda_weekday=tda_weekday)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        new_item = to_do_items.insert().values(item=request.form["item"], date=request.form["date"])
        
        with engine.connect() as conn:
            conn.execute(new_item)
            print("Works!")
        
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
