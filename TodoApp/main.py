from fastapi import FastAPI
from database import engine
import models



app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# This will create everything from our dayabase.py file and our models.py file to be able to create a new database that has a new table of Todos with all of the columns that we laid out in our models.py file.
