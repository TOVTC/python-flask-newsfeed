# the vote model doesn't need to store unique information
# it just references the post being upvoted and the id of the person who upvoted it
# the Post model will add up the records to get a total point value
from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))