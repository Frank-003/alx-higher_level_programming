#!/usr/bin/python3
"""Module that interacts with a MySQL database using SQLAlchemy to print states and their cities."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

def list_states_and_cities(username, password, db_name):
    # Connect to MySQL server
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and their corresponding City objects, sorted by states.id and cities.id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_and_cities(username, password, db_name)
