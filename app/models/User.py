from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
# use bcrypt for password encryption
# we want to directly use the bcrypt module, so the import syntax is different
import bcrypt

salt = bcrypt.gensalt()

# when using SQLAlchemy, we create models as Python classes
# python classes can also inherit from other classes
# here, Base is the parent class which was declared in the db package
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    # ORMs allow validation of data before inserting them into the database
    # validate_email() returns the value of what the email should be, and the @validates() decorator handles the rest
    @validates('email')
    def validate_email(self, key, email):
        # make sure the email address contains @ character
        # the assert keyword automatically throws an error if a condition is false, preventing the return statement from executing
        assert '@' in email

        return email
    
    # this will return an encrypted password if the validation does not throw an error
    @validates('password')
    def validate_password(self, key, password):
        # throw an error if fewer than four characters
        assert len(password) > 4

        return bcrypt.hashpw(password.encode('utf-8'), salt)
