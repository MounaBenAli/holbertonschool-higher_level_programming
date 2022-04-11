#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa using ORM
"""

from distutils.command.build_scripts import first_line_re


if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./7.py <username> <password> <database>")
        exit(1)

    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_line = session.query(State.id, State.name).first()
    if first_line is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_line[0], first_line[1]))
    session.close()
