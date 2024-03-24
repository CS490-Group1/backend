from account_storage import engine, Base
from sqlalchemy import text
from typing import List, Optional
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, insert
from datetime import datetime

class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    email = Column(String(128))
    first_name = Column(String(64))
    last_name = Column(String(64))
    dob = Column(Date)
    role = Column(Integer)
    drivers_license = Column(String(128))
    phone = Column(String(15))
    created = Column(TIMESTAMP)
    last_updated = Column (TIMESTAMP)
    notes = Column(String(256))

class Authentication(Base):
    __tablename__ = "authentication"
    auth_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    password = Column(String(256))
    created = Column(TIMESTAMP)
    last_updated = Column(TIMESTAMP)
    notes = Column(String(256))

    user = relationship("User", back_populates="authentication")

def store_customer(customer):
    created_id = 0
    time = datetime.now()
    customer = Users(email=customer.email, first_name=customer.first_name, last_name=customer.last_name, dob=customer.dob, 
                drivers_license=customer.drivers_license, phone=customer.phone, created=time, last_updated=time, notes='')
    customer.password = [Authentication(password=customer.password, created=time, last_updated=time, notes='')]
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        created_id = session.query(Users.user_id).filter(Users.email==customer.email).all()[0][0]
    return created_id

def grab_customer(login):
    with Session(engine) as session:
        return session.query(Authentication.password).join(Users).filter(email=login.email).all()[0][0]