from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # this foreign key references the users table
    user_id = Column(Integer, ForeignKey('users.id'))
    # built-in datetime modules generates timestamps
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # we want our data to be returned as JSON
    # we can define dynamic properties that won't become part of the MySQL table but will be returned with the JSON
    # here, there are two defined relationships for users and comments, which means querying a post returns both data subsets
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    # this will dynamically sum up the number of records associated with this comment in the Vote model
    # when we query the model, this dynamic property will perform a SELECT and SQLAlchemy func.count() operation
    votes = relationship('Vote', cascade='all,delete')
    vote_count = column_property(select(func.count(Vote.id)).where(Vote.post_id == id))