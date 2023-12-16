#!/usr/bin/python3

"""
A script that takes in an argument and display
all values in the states table of hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

def main():
    username = argv[1]
    password = argv[2]
    database = argv[3]

if __name__ == '__main__':
    """
    Accesses the database and retrieve states
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
