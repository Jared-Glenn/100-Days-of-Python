from flask import Flask, render_template, jsonify, request, redirect, url_for
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, create_engine
from sqlalchemy.orm import registry
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL, Regexp
import csv
import datetime
from os.path import exists


# Create the App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'anything'
# Configure the SQLite Database
engine = create_engine("sqlite+pysqlite:///C:/Users/Jared/Documents/3. Programming/100 Days of Python/Days 76-100/088_adjutant/instances/todo.db", echo=True, future=True)
mapper_registry = registry()
Base = mapper_registry.generate_base()

global_focus = datetime.date.today()


if not exists("C:/Users/Jared/Documents/3. Programming/100 Days of Python/Days 76-100/088_adjutant/instances/todo.db"):
    class Item(Base):
        __tablename__ = "todo_list"

        id = Column(Integer, primary_key=True)
        name = Column(String(30))
        date = Column(String)

        def __repr__(self):
            return f"Item(id={self.id!r}, name={self.name!r}, date={self.date!r})"


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
        new_item = Item(name=request.form["item"], fullname=request.form["date"])

    mapper_registry.metadata.create_all(engine)
    Base.metadata.create_all(engine)
        
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
