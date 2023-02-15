import sqlalchemy as db
from sqlalchemy import *

engine = db.create_engine("sqlite:///datacamp.sqlite")
conn = engine.connect()

metadata = db.MetaData()

Student = db.Table('Student', metadata,
                   db.Column('Id', db.Integer(), primary_key=True),
                   db.Column('Name', db.String(255), nullable=False),
                   db.Column('Major', db.String(255), default='Math'),
                   db.Column('Pass', db.Boolean(), default=True)
                   )

metadata.create_all(engine)

for x in range(3):
    print("New!")

query = db.insert(Student).values(Id=1, Name='Matthew', Major='English', Pass=True)
Result = conn.execute(query)

output = conn.execute(Student.select()).fetchall()
print(output)

query = db.insert(Student)
values_list = [{'Id':'2', 'Name':'Nisha', 'Major':'Science', 'Pass':False},
               {'Id':'3', 'Name':'Natasha', 'Major':'Math', 'Pass':True},
               {'Id':'4', 'Name':'Ben', 'Major':'English', 'Pass':False}]
Result = conn.execute(query, values_list)

output = conn.execute(db.select([Student])).fetchall()
print(output)
