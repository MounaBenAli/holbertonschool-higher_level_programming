#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    databasename = argv[3]

    database = MySQLdb.Connect(user=username, passwd=password , db=databasename, port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for row in states:
        print(row)
