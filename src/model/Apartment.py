from .base import Base
from sqlalchemy import Column, Integer, String

class Apartment(Base):
  __tablename__: str = 'apartments'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, nullable=False)
  number_of_people = Column(Integer, nullable=False)