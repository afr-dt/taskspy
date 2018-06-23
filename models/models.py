from sqlalchemy import Table, Column, DateTime, Time, Date, ForeignKey, Integer, String, Float, func, Boolean, Numeric, insert, Text
from sqlalchemy.orm import backref, relationship

from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert

from config import Base
from config import db_session


class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20))
    surname = Column(String(20))


class Task(Base):
    __tablename__ = 'Tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    description = Column(Text)
    timer = Column(Integer)
    status = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.utc_timestamp())
