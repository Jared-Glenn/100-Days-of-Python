from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL, Regexp
import csv
import datetime

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'anything'
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

global_focus = datetime.date.today()


db.create_all()

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




if __name__ == '__main__':
    app.run(debug=True)
