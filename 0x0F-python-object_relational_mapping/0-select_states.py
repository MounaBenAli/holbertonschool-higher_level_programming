#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    usr = argv[1]
    pwd = argv[2]
    dbe = argv[3]

conn = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=usr,
                       passwd=pwd,
                       db=dbe,
                       charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
