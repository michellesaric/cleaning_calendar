from .base import Base
from sqlalchemy import Column, Integer,String

class User(Base):
  __tablename__: str = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)