#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

from logging import root


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)

    root = argv[1]
    passwd = argv[2]
    hbtn_0e_0_usa = argv[3]

    database = MySQLdb.Connect(
        user=root,
        passwd='',
        db='hbtn_0e_0_usa',
        port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for row in states:
        print(row)
