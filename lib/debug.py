#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Base, Company, Dev, Freebie 

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/freebies.db')

    print("Creating database tables if they don't exist...")

    Base.metadata.create_all(engine)
    print("Database table creation process complete.")

    import ipdb; ipdb.set_trace()

   