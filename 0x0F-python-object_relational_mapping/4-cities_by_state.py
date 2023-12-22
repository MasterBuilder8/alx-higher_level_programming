#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa"""

import  MySQLdb
import sys


if __name__ == "__main__":
    connct = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                 FROM 'states' \
                 WHERE BINARY 'name' = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
