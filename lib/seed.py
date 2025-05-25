#!/usr/bin/env python3

# Script goes here!

#!/usr/bin/env python3

# Script goes here!
from models import Dev, Company, Freebie, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine =create_engine('sqlite://freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# Clear out old data for a fresh start
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create companies
c1 = Company(name="Highlands Drinks", founding_year=1954)
c2 = Company(name="Jitu", founding_year=2010)
c3 = Company(name="Safaricom", founding_year=1997)

# Create devs
d1 = Dev(name="Joan")
d2 = Dev(name="Ella")
d3 = Dev(name="Kori")

# Add and commit to get IDs assigned
session.add_all([c1, c2, c3, d1, d2, d3])
session.commit()

# Create freebies (each links dev and company)
f1 = Freebie(item_name="Tote bag", value=20, dev_id=d1.id, company_id=c1.id)
f2 = Freebie(item_name="Hoodies", value=15, dev_id=d2.id, company_id=c2.id)
f3 = Freebie(item_name="T-shirts", value=21, dev_id=d1.id, company_id=c3.id)
f4 = Freebie(item_name="Ear pods", value=9, dev_id=d3.id, company_id=c1.id)
f5 = Freebie(item_name="Notebook", value=7, dev_id=d2.id, company_id=c3.id)
f6 = Freebie(item_name="Pen", value=19, dev_id=d3.id, company_id=c2.id)

session.add_all([f1, f2, f3, f4, f5, f6])
session.commit()

print("Database seeded!")