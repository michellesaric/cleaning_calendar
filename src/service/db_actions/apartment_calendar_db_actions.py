import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.Apartment import Apartment
from model.ApartmentCalendar import ApartmentCalendar
from service.db_actions.apartment_db_actions import create_apartment

def create_apartment_calendar(db: Session, apartment_name: str, number_of_people: int, start_date: datetime, end_date: datetime):
  apartment = db.query(Apartment).filter(Apartment.name == apartment_name).first()

  if not apartment:
    apartment = create_apartment(db, apartment_name, number_of_people)
  
    apartment_calendar = ApartmentCalendar(
      apartment_id=apartment.id,
      start_date=start_date,
      end_date=end_date
    )
    db.add(apartment_calendar)
    db.commit()
    db.refresh(apartment_calendar)

    return {"message": "Apartment calendar created successfully", "apartment_calendar_id": apartment_calendar.id}

def get_all_calendars(db: Session):
  calendars = db.query(ApartmentCalendar, Apartment.name, Apartment.number_of_people) \
    .join(Apartment, Apartment.id == ApartmentCalendar.apartment_id) \
    .all()

  if not calendars:
    raise HTTPException(status_code=404, detail="No calendars found")

  return [{
    "id": calendar.id,
    "name": name,
    "number_of_people": number_of_people,
    "start_date": calendar.start_date,
    "end_date": calendar.end_date
  } for calendar, name, number_of_people in calendars]

def get_calendar_by_id(db: Session, calendar_id: int):
  calendars = db.query(ApartmentCalendar, Apartment.name, Apartment.number_of_people) \
    .join(Apartment, Apartment.id == ApartmentCalendar.apartment_id) \
    .filter(Apartment.id == calendar_id) \
    .all()

  if not calendars:
    raise HTTPException(status_code=404, detail="Calendar not found")

  return [{
    "id": calendar.id,
    "name": name,
    "number_of_people": number_of_people,
    "start_date": calendar.start_date,
    "end_date": calendar.end_date
  } for calendar, name, number_of_people in calendars]