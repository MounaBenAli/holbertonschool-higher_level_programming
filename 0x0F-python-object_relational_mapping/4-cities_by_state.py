#!/usr/bin/python3
"""
Script lists all cities from the database hbtn_0e_4_usa
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
    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            WHERE cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cursor.execute(query)
    cities = cursor.fetchall()
    for row in cities:
        print(row)
    cursor.close()
    database.close()
