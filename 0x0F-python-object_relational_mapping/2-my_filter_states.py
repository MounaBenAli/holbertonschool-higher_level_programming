#!/usr/bin/python3
"""
Script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: ./2.py <username> <password> <database> <input>")
        exit(1)

    username = argv[1]
    password = argv[2]
    databasename = argv[3]
    input = argv[4]

    database = MySQLdb.Connect(
        user=username,
        passwd=password,
        db=databasename,
        port=3306)
    cursor = database.cursor()
    cursor.execute("""
        SELECT * FROM states WHERE states.name LIKE '%{:s}%'
        ORDER BY states.id ASC
        """.format(input))
    states = cursor.fetchall()
    for row in states:
        print(row)
    cursor.close()
    database.close()
