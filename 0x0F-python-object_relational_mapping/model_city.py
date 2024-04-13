#!/usr/bin/python3
#Define a city model.
#inherit from SQLAlchemy base and links to the MySQl table cities.
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
