#!/usr/bin/python3
"""MOdule that lists all the states from hbtn_0e_0_usa database."""
import MySQLdb
import sys

    if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()

        c.execute("SELECT *\
                    FROM `states` \
                    WHERE BINARY `name` = '{}'".format{sys.argv[4]))

        [print(state) for state in c.fetchall()]
