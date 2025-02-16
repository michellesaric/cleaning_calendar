import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.Apartment import Apartment
from model.ApartmentCalendar import ApartmentCalendar

def create_apartment_calendar(db: Session, apartment_id: int, start_date: datetime, end_date: datetime, name_of_reservation: str):
  apartment = db.query(Apartment).filter(Apartment.id == apartment_id).first()

  if not apartment:
    raise HTTPException(status_code=400, detail="Apartment missing")
  
  apartment_calendar = ApartmentCalendar(
    apartment_id=apartment_id,
    start_date=start_date,
    end_date=end_date,
    name_of_reservation=name_of_reservation
  )
  db.add(apartment_calendar)
  db.commit()
  db.refresh(apartment_calendar)

  return {"message": "Apartment calendar created successfully", "apartment_calendar_id": apartment_calendar.id}

def get_all_calendars(db: Session, user_id: int):
  reservations = db.query(ApartmentCalendar, Apartment.name, Apartment.user_id) \
    .join(Apartment, Apartment.id == ApartmentCalendar.apartment_id) \
    .filter(Apartment.user_id == user_id) \
    .all()

  if not reservations:
    raise HTTPException(status_code=404, detail="No calendars found")

  return [{
    "id": reservation.id,
    "name": name,
    "start_date": reservation.start_date,
    "end_date": reservation.end_date,
    "name_of_reservation": reservation.name_of_reservation
  } for reservation, name, _ in reservations]

def get_calendar_by_id(db: Session, calendar_id: int, user_id: int):
  reservations = db.query(ApartmentCalendar, Apartment.name, Apartment.user_id) \
    .join(Apartment, Apartment.id == ApartmentCalendar.apartment_id) \
    .filter(Apartment.id == calendar_id) \
    .all()

  if not reservations:
    raise HTTPException(status_code=404, detail="Calendar not found")
  
  _, _, user_id = reservations[0]
  if user_id != user_id:
    raise HTTPException(status_code=403, detail="Unauthorized to use this calendar")

  return [{
    "id": reservation.id,
    "name": name,
    "start_date": reservation.start_date,
    "end_date": reservation.end_date,
    "name_of_reservation": reservation.name_of_reservation
  } for reservation, name, _ in reservations]

# def check_for_overlapping_dates(db: Session, apartment_id: int, start_date: datetime, end_date: datetime):
#   return db.query(ApartmentCalendar).filter(
#     ApartmentCalendar.apartment_id == apartment_id,
#     ApartmentCalendar.start_date < end_date,
#     ApartmentCalendar.end_date >= start_date
#   ).first()