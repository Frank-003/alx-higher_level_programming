#!/usr/bin/python3
"""Module that deletes all states object contataining letter "a" from MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, db_name):
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:

        state_to_update.name = 'New Mexico'
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with id=2 not found.")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    change_state_name(username, password, db_name)

