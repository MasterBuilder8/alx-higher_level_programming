#!/usr/bin/python3

"""
A script that list all state with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Acess the database and  retrieve all states
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE BINARY 'N%'\
                 ORDER by states.id ASC")
    row = cur.fetchall()

    for row in rows:
        print(row)
