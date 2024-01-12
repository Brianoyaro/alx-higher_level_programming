#!/usr/bin/python3
"""7-model_state_fetch_all.py module"""
from state_model import Base, State
import sys
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
"""create a new sessioni to manage your tranasction"""
session = Sessio(engine)
for state in session.query(States).order_by(state_id).all():
    print(state)
"""close the session"""
session.close()
