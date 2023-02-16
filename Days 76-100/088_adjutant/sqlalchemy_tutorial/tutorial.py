from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, select, insert
from sqlalchemy.orm import Session, registry, relationship

engine = create_engine("sqlite+pysqlite:///tutorial.db", echo=True, future=True)
metadata_obj = MetaData()

# with engine.connect() as conn:
#     result=conn.execute(text("select 'hello world'"))
#     print(result.all())

# # Commit as you go
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x":1, "y":1}, {"x":2, "y":4}]
#     )
#     conn.commit()

# # Begin once
# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x":6, "y":8}, {"x": 9, "y":10}],
#     )
    
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     for row in result:
#         print(f'x: {row.x} y: {row.y}')
        
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y":2})
#     for row in result:
#         print(f"x: {row.x} y: {row.y}")


# with engine.connect() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
#     )
#     conn.commit()
    
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     for row in result:
#         print(f'x: {row.x} y: {row.y}')


# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
# with Session(engine) as session:
#     result = session.execute(stmt, {"y": 6})
#     for row in result:
#         print(f"x: {row.x} y: {row.y}")


# with Session(engine) as session:
#     result = session.execute(
#         text("UPDATE some_table SET y=:y WHERE x=:x"),
#         [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
#     )
#     session.commit()




# user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String),
# )


# print(user_table.c.name)

# print(user_table.c.keys())

# print(user_table.primary_key)

# address_table = Table(
#     "address",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", ForeignKey("user_account.id"), nullable=False),
#     Column("email_address", String, nullable=False),
# )




# mapper_registry = registry()

# Base = mapper_registry.generate_base()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

metadata_obj.create_all(engine)

# class User(Base):
#     __table__ = user_table
#     __table_args__ = {'extend_existing': True}
    
#     def __repr__(self):
#         return f"User(name={self.name!r}, fullname={self.fullname!r})"
    
    
# sandy = User(name="sandy", fullname="Sandy Cheeks")

# metadata_obj.create_all(engine)

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")

# compiled = stmt.compile()


with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()


# print(result.inserted_primary_key)

