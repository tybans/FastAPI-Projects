from database import Base
from sqlalchemy import  Column, Integer, String, Boolean


# creating table
class Todos(Base):
    __tablename__ = 'todos'

    id= Column(Integer, primary_key=True, index=True)
    title= Column(String)
    description= Column(String)
    priority= Column(Integer)
    complete= Column(Boolean, default=False)




# Model is a way for SQLAlchemy to be able to understand what kind of database tables we are going to be creating within our database in the future.
# A database model is going to be the actual record that is inside a database table.
