#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306,
                         charset="utf8")

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id"""

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
