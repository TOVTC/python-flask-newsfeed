# getenv is part of Python's built in os module
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# flask has application contexts which are created and removed every time a server response is made and completed
# the temporary contexts provide global variables, such as g, which can be shared across modules as long as the context is active
from flask import g

# we used .env to fake an environment variable here so we need to call this first
# in production, DB_URL would be a proper environment variable
load_dotenv()

# connect to database using env variable
# engine manages the overall connection to the database
# Session generates temporary connections for performing CRUD operations
# Base class helps map the models to real MySQL tables
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# this is the same create_all() method from the seeds page, but it won't be executed until init_db() is called
def init_db(app):
    Base.metadata.create_all(engine)

    # with the built-in teardown_appcontext() method, the db connection will be closed automatically
    app.teardown_appcontext(close_db)

# whenever return Session() is called, it returns a new session-connection object
# Session can be directly imported from the db package into other modules but
# this function allows us to perform additional logic before creating the database connection
# here, we use the global variable g so we can avoid creating duplicate new session connections
def get_db():
    if 'db' not in g:
        # store db connection in appcontext
        g.db = Session()
    return g.db

# we need to close the database connection every time we are done with it, otherwise it can cause the app to crash
# (we can't have an infinite number of open connections)
def close_db(e=None):
    # attempt to find and remove db from the g object
    db = g.pop('db', None)

    # then, if db exists, close it
    if db is not None:
        db.close()