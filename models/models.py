from sqlalchemy import Table, Column, DateTime, Time, Date, Integer, String, func, Boolean, Text
from sqlalchemy.orm import backref, relationship

from sqlalchemy.dialects import postgresql
import datetime

from config import Base
from config import db_session


class Task(Base):
    __tablename__ = 'Tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    description = Column(Text)
    timer = Column(Integer)
    status = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=datetime.datetime.now)
