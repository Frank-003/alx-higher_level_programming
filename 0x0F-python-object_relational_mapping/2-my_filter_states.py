#!/usr/bin/python3
"""Module that lists all the states from hbtn_0e_0_usa database."""
import sys
import MySQLdb

    if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", user.sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
        c = db.cursor()

        c.execute("SELECT *\FROM `states` \WHERE BINARY `name` = '{}'"
                .format{sys.argv[4]))
        rows = c.fetchall()
        for row in rows:
            print(row)
            c.close()
            db.close()
