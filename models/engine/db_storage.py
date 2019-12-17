#!/usr/bin/python3
from sqlalchemy import create_engine


# Review if is a class.
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(),
        pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
