#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
        cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
