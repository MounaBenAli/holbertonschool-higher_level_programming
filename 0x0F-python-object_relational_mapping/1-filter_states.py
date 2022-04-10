#!/usr/bin/python3
"""
lists all states with starting name (upper N) from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    databasename = argv[3]

    database = MySQLdb.Connect(
        user=username,
        passwd=password,
        db=databasename,
        port=3306)
    cursor = database.cursor()
    cursor.execute("""
            SELECT * FROM states WHERE states.name LIKE 'N%'
            ORDER BY states.id ASC
            """)
    states = cursor.fetchall()
    for row in states:
        if (row[1][0] == 'N'):
            print(row)
    cursor.close()
    database.close()
