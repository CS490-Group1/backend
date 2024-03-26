from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
engine = create_engine('mysql+pymysql://flx2:StrongPassword!@490sakila.mysql.database.azure.com/dealership', echo=True)

class Base(DeclarativeBase):
    pass