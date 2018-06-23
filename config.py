from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine('sqlite:///api.sqlite3', convert_unicode=True)
engine = create_engine(
    'postgresql://afr:d3VDJ4n60OneD4yIwalk4lon3@localhost/graphqltask', convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models.models import User, Task
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db_session.commit()
