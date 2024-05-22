# getenv is part of Python's built in os module
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

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