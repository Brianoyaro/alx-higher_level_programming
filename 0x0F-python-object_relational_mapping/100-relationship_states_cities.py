#!/usr/bin/python3
"""100-model_state_fetch_all.py module"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    """create a session factory"""
    Session = sessionmaker(bind=engine)
    """create a new session to manage your tranasction"""
    session = Session()

    stateee = State()
    stateee.name = "California"
    cityyy = City()
    city_.name = "San Francisco"
    state.cities.append(cityyy)
    session.add(state_)
    session.add(city_)

    session.commit()

    """close the session"""
    session.close()
