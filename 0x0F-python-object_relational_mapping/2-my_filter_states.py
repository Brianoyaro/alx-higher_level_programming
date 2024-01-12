#!/usr/bin/python3
"""odule showcasing usage of mysqldb
"""
import MySQLdb
import sys


arg = sys.argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
            port=3306,
            user=arg[1],
            passwd=arg[2],
            db=arg[3])
"""create a connection to the database"""
curr = conn.cursor
curr.execute("SELECT * FROM states\
        WHERE name LIKE '{}%'\
        ORDER BY states.id ASC".format(arg[4])
"""fetch query results"""
rows = curr.fetchall()
for row in rows:
    print(row)
"""close cursor connection"""
curr.close()
"""close database connection"""
conn.close()
