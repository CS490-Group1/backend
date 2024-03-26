from data.alchemy_setup import engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import datetime
from data.alchemy_classes import Users, Authentication, Cars, Owned

def store_customer(customer):
    created_id = 0
    time = datetime.now()
    user = Users(
        email=customer.email,
        first_name=customer.first_name,
        last_name=customer.last_name,
        dob=customer.dob, 
        drivers_license=customer.drivers_license,
        phone=customer.phone,
        created=time,
        last_updated=time, notes=''
    )

    auth = Authentication(
        password=customer.password,
        created=time,
        last_updated=time,
        notes=''
    )
    auth.users = user
    with Session(engine) as session:
        email_exist = session.query(Users.user_id).filter(Users.email==customer.email).all()
        if(len(email_exist)):
            return False
        session.add(user)
        session.add(auth)
        session.commit()
        created_id = session.query(Users.user_id).filter(Users.email==customer.email).all()[0][0]
    return created_id

def change_customer(customer, user_id):
    time = datetime.now()
    user = {
        "email":customer.email,
        "first_name":customer.first_name,
        "last_name":customer.last_name,
        "dob":customer.dob, 
        "drivers_license":customer.drivers_license,
        "phone":customer.phone,
        "last_updated":time
    }
    with Session(engine) as session:
        session.query(Users).filter(Users.user_id==user_id).update(user)
    return user_id

def grab_customer(login):
    with Session(engine) as session:
        return session.query(Authentication.password).join(Users).filter(Users.email==login).all()[0][0]

def change_password(info):
    with Session(engine) as session:
        session.query(Authentication).join(Users).filter(Users.email==info.email).update({Authentication.password: info.new_password})
        session.commit()
    return info
    
def get_owned_cars(user_id):
    with Session(engine) as session:
        return session.query(Cars.car_id, Cars.make, Cars.model, Cars.year, Cars.color, Cars.type, Cars.mpg, Cars.image).join(Owned).filter(Owned.user_id==user_id).all()