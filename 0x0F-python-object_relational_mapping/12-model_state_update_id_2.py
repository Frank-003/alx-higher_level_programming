#!/usr/bin/python3
"""Module that updates the name of the states in a MySQL data base using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database):
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state_to_change = session.query(State).filter(State.id == 2).first()

    # Check if state with id = 2 exists
    if state_to_change:
        # Change the name of the state
        state_to_change.name = "New Mexico"
        session.commit()
        print("State name changed successfully.")
    else:
        print("State with id = 2 not found.")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to change state name
    change_state_name(username, password, database)

