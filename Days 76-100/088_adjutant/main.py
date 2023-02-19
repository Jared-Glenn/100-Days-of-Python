from flask import Flask, render_template, jsonify, request, redirect, url_for
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float, create_engine, ForeignKey, select, insert, delete, update
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
metadata_obj = MetaData()

global_focus = datetime.date.today()


todo_list = Table(
    "todo_item",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("date", String(100)),
    Column("checked", Boolean)
)

metadata_obj.create_all(engine)

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
    
    # Day Before Items
    db_list_data = select(todo_list).where(todo_list.c.date == day_before)
    db_dict = []
    with engine.connect() as conn:
        for row in conn.execute(db_list_data):
            db_dict.append((row[1], row[3]))
    
    # Focus Items
    focus_list_data = select(todo_list).where(todo_list.c.date == focus)
    focus_dict = []
    with engine.connect() as conn:
        for row in conn.execute(focus_list_data):
            focus_dict.append((row[1], row[3]))
    
    # Day After Items
    da_list_data = select(todo_list).where(todo_list.c.date == day_after)
    da_dict = []
    with engine.connect() as conn:
        for row in conn.execute(da_list_data):
            da_dict.append((row[1], row[3]))
    
    # Two Days After Items
    tda_list_data = select(todo_list).where(todo_list.c.date == two_days_after)
    tda_dict = []
    with engine.connect() as conn:
        for row in conn.execute(tda_list_data):
            tda_dict.append((row[1], row[3]))
            
    # Delete Old Items
    clean_up = delete(todo_list).where(todo_list.c.date != day_before).where(todo_list.c.date != focus).where(
                                       todo_list.c.date != day_after).where(todo_list.c.date != two_days_after)
    with engine.connect() as conn:
            result = conn.execute(clean_up)
            conn.commit()
        
    
    return render_template("index.html", focus=focus_str, f_weekday=f_weekday, day_before=day_before_str, db_weekday=db_weekday,
                           day_after=day_after_str, da_weekday=da_weekday, two_days_after=two_days_after_str,
                           tda_weekday=tda_weekday, f_num=focus, db_num=day_before, da_num=day_after, 
                           tda_num=two_days_after, db_dict=db_dict, focus_dict=focus_dict, da_dict=da_dict,
                           tda_dict=tda_dict)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        stmt = insert(todo_list).values(name=request.form["item"], date=request.form["date"], checked=False)

        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        
        
    # print("STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING")
    
    return redirect(url_for('home'))

@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method=="POST":
        item_checking = select(todo_list).filter_by(name=request.form["item"])
        with engine.connect() as conn:
            result = conn.execute(item_checking)
        
        print("INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO INFO")
        print(result)
        
        # if 0 == False:
        #     stmt = (update(todo_list).where(todo_list.c.name == request.form["item"]).values(checked="True"))
        # elif 1 == True:
        #     stmt = (update(todo_list).where(todo_list.c.name == request.form["item"]).values(checked="False"))
        
        # with engine.connect() as conn:
        #     result = conn.execute(stmt)
        #     conn.commit()
        
        
    # print("STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING STARTING")
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
