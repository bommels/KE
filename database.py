from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlite2.db', echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
db = Session()


def init_db():
    Base.metadata.create_all(engine)
