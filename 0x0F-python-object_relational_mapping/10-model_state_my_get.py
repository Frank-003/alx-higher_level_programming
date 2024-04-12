#!/usr/bin/python3
"""Module that retrieve searches for  a stata in a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_state_by_name(username, password, database, state_name):
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to print state by name
    print_state_by_name(username, password, database, state_name)

