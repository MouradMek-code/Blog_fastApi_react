from sqlalchemy import Column, Integer, DateTime, String

from .database import  Base

class DbPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    image_url = Column(String)
    creator=Column(String)
    timestamp=Column(DateTime)