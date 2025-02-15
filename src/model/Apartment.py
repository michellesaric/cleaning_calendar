from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String

class Apartment(Base):
  __tablename__: str = 'apartments'
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('apartments.id', ondelete="CASCADE"), nullable=False)
  name = Column(String, unique=True, nullable=False)