#!/usr/bin/python3
""""Module that adds a new state a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

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

    # Call the function to add state
    add_state(username, password, database)
