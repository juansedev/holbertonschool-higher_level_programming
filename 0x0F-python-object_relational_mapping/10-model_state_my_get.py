#!/usr/bin/python3
"""Start link class to table in database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


if __name__ == "__main__":

    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'. \
        format(argv[1], argv[2], argv[3])

    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    state_name = argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
