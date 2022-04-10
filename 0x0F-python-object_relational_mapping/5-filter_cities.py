#!/usr/bin/python3
"""
Script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: ./5.py <username> <password> <database> <state_name>")
        exit(1)

    username = argv[1]
    password = argv[2]
    databasename = argv[3]
    state_name = argv[4]

    database = MySQLdb.Connect(
        user=username,
        passwd=password,
        db=databasename,
        port=3306)

    cursor = database.cursor()
    query = """ SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    new = []
    for row in cities:
        new.append(row[0])
    print(", ".join(new))
    cursor.close()
    database.close()
