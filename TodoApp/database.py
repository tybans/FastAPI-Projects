from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABSE_URL = 'sqlite:///./todos.db'

# Now, this URL is going to be used to be able to create a location of this database on our fastapi application


engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={'check_same_thread': False})

# A database engine is something that we can use to be able to open up a connection and be able to use our database
# The connect_args are arguments that we can pass into our create engine , which will allow au to be able to define some kind of connection to a database.
# By default, SQLite will only allow one thread to communicate with it.
# Assuming that each thread will handle an independent request.
# This is to prevent any kind of accident sharing of the same connection for different kind of requests.
# But in fastapi it's very normal to have more than one thread that could interact with the database at the same time.
# So, we just need to make sure SQLite knows that hey, we don't want to be checking the same thread all the time because there could be multiple threads happening to our SQLite database



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session Loacl: Each instance of the session local will have a database session.
# The class itself is not a database session yet we will add that later on.
# right now we just need to be able to create an instance of session local that will be able to become an actual database in the future 

# We want to bind to the engine that we just created and we want to make sure that our auto commits and auto flush are false OR the database transactions are going to try and do something automatically.
# We want to be fully control of everything our database will do in the future


# Creating a database object, which will be able to interact with the tables that we create in the future
Base = declarative_base()