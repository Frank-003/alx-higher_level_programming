#!/usr/bin/python3
"""Module that lists all states from hbtn_0e_4_usa database."""

import MySQLdb
import sys

if__name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],passwd=sys.argv[2], db=sys[3], port=3306)

    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s""", (sys.argv[4].))
    rows = c.fetchall()
    tmp = list(row[0] for row in row)
    print(*tmp, sep=", ")
    c.close()
    db.close()
