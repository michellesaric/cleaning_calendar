from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, CheckConstraint

class ApartmentCalendar(Base):
  __tablename__: str = 'apartment_calendar'
  id = Column(Integer, primary_key=True, index=True)
  apartment_id = Column(Integer, ForeignKey('apartments.id', ondelete="CASCADE"), nullable=False)
  start_date = Column(DateTime, nullable=False)
  end_date = Column(DateTime, nullable=False)

  __table_args__ = (
    CheckConstraint("end_date > start_date", name="check_end_after_start"),
  )