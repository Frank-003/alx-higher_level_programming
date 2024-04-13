#!/usr/bin/python3
"""Module that adds a city and its associated state to  a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_state_and_city(username, password, db_name):
    # Connect to MySQL server
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')

    # Create tables if not exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if California already exists
    california = session.query(State).filter_by(name='California').first()
    if california is None:
        # Create California state
        california = State(name='California')
        session.add(california)
        session.commit()

    # Check if San Francisco already exists
    san_francisco = session.query(City).filter_by(name='San Francisco').first()
    if san_francisco is None:
        # Create San Francisco city and link to California state
        san_francisco = City(name='San Francisco', state=california)
        session.add(san_francisco)
        session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    create_state_and_city(username, password, db_name)

