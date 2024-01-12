#!/usr/bin/python3
"""7-model_state_fetch_all.py module"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    """create a session factory"""
    Session = sessionmaker(bind=engine)
    """create a new session to manage your tranasction"""
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states:
        print("{}: {}".fomat(state.id, state.name))
    """close the session"""
    session.close()