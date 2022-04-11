#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa using ORM
"""

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./7.py <username> <password> <database>")
        exit(1)

    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    eng = "mysql://" + user + ":" + passwd + "@localhost:3306/" + database
    engine = create_engine(eng)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for state in query.all():
        print("{} : {}".format(state.id, state.name))
    session.close()
