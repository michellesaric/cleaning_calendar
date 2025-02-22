from sqlalchemy import Column, ForeignKey, Integer, String
from .base import Base

class Apartment(Base):
  __tablename__: str = 'apartments'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
  name = Column(String, unique=True, nullable=False)