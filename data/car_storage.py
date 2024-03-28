from data.alchemy_setup import engine
from sqlalchemy.orm import Session
from datetime import datetime
from data.alchemy_classes import Cars, Owned

def get_available_cars():
    with Session(engine) as session:
        result = session.query(Cars).join(Owned).filter(Cars.car_id!=Owned.car_id and Cars.available==1)
    return result

def store_car(car):
    created_id = 0
    time = datetime.now()
    car = Cars(
        make=car.make,
        model=car.model,
        year=car.year,
        color=car.color, 
        type=car.type,
        mpg=car.mpg,
        price=car.price,
        available=car.available,
        image=car.image,
        created=time,
        last_updated=time, notes=''
    )
    with Session(engine) as session:
        session.add(car)
        session.commit()
        created_id = car.car_id
    return created_id