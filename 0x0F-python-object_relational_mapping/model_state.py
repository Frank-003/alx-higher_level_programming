#!/usr/bin/python3
"""Module that  defines the class representing a state in a MySQL database."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for MySQL database.

    __tablename__(str): The name of the MySQL table to store table.
    id (sqlalchemy.integer): The state's id.
    name (sqlalchemy.string): The state's name."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
