#!/usr/bin/python3
"""Module that retrieve and prints all cities along with their associated states from a MySQL database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_all_cities(username, password, db_name):
    # Connect to MySQL server
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_all_cities(username, password, db_name)

