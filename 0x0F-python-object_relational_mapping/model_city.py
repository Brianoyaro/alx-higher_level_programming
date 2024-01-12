#!/usr/bin/python3
"""model_city module"""
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


"""declare base"""
Base = declarative_base()


class City(Base):
    """state class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey(State.id))
