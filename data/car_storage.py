from data.alchemy_setup import engine
from sqlalchemy.orm import Session
from datetime import datetime
from data.alchemy_classes import Cars, Owned

def get_available_cars():
    with Session(engine) as session:
        result = session.query(Cars).join(Owned).filter(Cars.car_id!=Owned.car_id and Cars.available==1)
    return result