from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///lib/freebies.db')

Base = declarative_base(metadata=metadata)


#Company table
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    
    #relationship- backref automatically creates the reverse reference
    freebies = relationship('Freebie', backref='company')

    def __repr__(self):
        return f'<Company {self.name}>'
    
    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()
        return new_freebie
    
    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()



#Devs table
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    #relationship
    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()
            return True
        return False


    
#Freebies table
class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    def __repr__(self):
        return f'<Freebie {self.item_name}>'
        
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."


Session = sessionmaker(bind=engine)
session = Session()
    