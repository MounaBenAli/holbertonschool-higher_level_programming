#!/usr/bin/python3
"""
prints  the State object with the name passed as argument
from the database hbtn_0e_6_usa using ORM.
"""


if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: ./7.py <username> <password> <database> <name>")
        exit(1)

    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
