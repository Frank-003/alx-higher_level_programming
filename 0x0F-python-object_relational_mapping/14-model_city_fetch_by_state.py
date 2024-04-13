#!/usr/bin/python3
"""Module that deletes states containing the letter "a" from MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": {" +(instance[1]) ") " +instance[2])
