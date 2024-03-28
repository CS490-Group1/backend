from data.alchemy_setup import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, DECIMAL, TIMESTAMP, ForeignKey

class Users(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    dob = Column(Date)
    role_id = Column(Integer, ForeignKey('user_roles.role_id'), default=1)
    drivers_license = Column(String(128))
    phone = Column(String(15))
    created = Column(TIMESTAMP)
    last_updated = Column (TIMESTAMP)
    notes = Column(String(256))
    authentication = relationship("Authentication", back_populates="users")
    user_cars = relationship("Owned", back_populates="users")
    user_roles = relationship("User_Roles", back_populates="users")

    def __repr__(self) -> str:
        return f"Users(user_id={self.user_id!r}, email={self.email!r} first_name={self.first_name!r}, last_name={self.last_name!r},\
        dob={self.dob}, role={self.role_id}, driverse_license={self.drivers_license}, phone={self.phone}, created={self.created},\
        last_update{self.last_updated}, notes={self.notes})"
    
class User_Roles(Base):
    __tablename__ = "user_roles"
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(32))
    created = Column(TIMESTAMP)
    last_updated = Column (TIMESTAMP)
    notes = Column(String(256))
    users = relationship("Users", back_populates="user_roles")

class Authentication(Base):
    __tablename__ = "authentication"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True,  autoincrement=True)
    password = Column(String(256))
    salt = Column(String(256))
    created = Column(TIMESTAMP)
    last_updated = Column(TIMESTAMP)
    notes = Column(String(256))

    users = relationship("Users", back_populates="authentication")
    def __repr__(self) -> str:
        return f"Authentication(auth_id={self.auth_id}, user_id={self.user_id!r}, password={self.password!r}, created={self.created},\
        last_update{self.last_updated}, notes={self.notes})"
    
class Cars(Base):
    __tablename__ = "cars"
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(32))
    model = Column(String(32))
    year = Column(String(4))
    color = Column(String(32))
    type = Column(String(32))
    mpg = Column(DECIMAL(3, 1))
    price = Column(DECIMAL(8, 2))
    available = Column(Integer)
    image = Column(String(128))
    created = Column(TIMESTAMP)
    last_updated = Column(TIMESTAMP)
    notes = Column(String(256))
    user_cars = relationship("Owned", back_populates="cars")

    def __repr__(self):
        return f"Car(car_id={self.car_id}, make={self.make}, model={self.model}, year={self.year}, color={self.color}, type={self.type},\
        mpg={self.mpg}, price={self.price}, available={self.available}, image={self.image}, created={self.created},\
        last_updated={self.last_updated}, notes={self.notes})"
    
class Owned(Base):
    __tablename__ = "owned"
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.car_id'), primary_key=True)
    created = Column(TIMESTAMP)
    last_updated = Column(TIMESTAMP)
    notes = Column(String(256))

    users = relationship("Users", back_populates="user_cars")
    cars = relationship("Cars", back_populates="user_cars")

    def __repr__(self):
        return f"UserCar(user_id={self.user_id}, car_id={self.car_id}, created={self.created}, last_updated={self.last_updated},\
        notes={self.notes})"