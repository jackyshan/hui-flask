from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

class Zixun(Base):
    __tablename__ = 'zixuns'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False)
    category = Column(String(50), unique=False)
    source = Column(String(50), unique=False)
    update_time = Column(String(50), unique=False)
    see_times = Column(Integer, unique=False)
    publish_status = Column(Integer, unique=False)

    def __init__(self, title=None, category=None, source=None, update_time=None, see_times=None, publish_status=None):
        self.title = title
        self.category = category
        self.source = source
        self.update_time = update_time
        self.see_times = see_times
        self.publish_status = publish_status

    def __repr__(self):
        return '<Zixun %r>' % (self.title)
