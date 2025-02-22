from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from ics import Calendar

from service.db_actions.apartment_db_actions import create_apartment
from service.db_actions.apartment_calendar_db_actions import create_apartment_calendar
from utils.is_valid_url import is_valid_url
from utils.confirm_datetime import confirm_datetime
from utils.get_ics_from_url import get_ics_from_url

async def import_calendar_from_ics_file(file: UploadFile, db: Session, user_id: int):
  try:
    content = await file.read()
    calendar = Calendar(content.decode("utf-8"))

    message = import_calendar(calendar.events, db, user_id)
    return message
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error processing ICS file: {str(e)}")

async def import_calendar_from_url(url:str, db:Session, user_id: int):
  try:
    if not is_valid_url(url):
      raise HTTPException(status_code=400, detail="Invalid URL format")
    
    calendar = get_ics_from_url(url)

    return import_calendar(calendar.events, db, user_id)
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error processing ICS URL: {str(e)}")


def import_calendar(events, db:Session, user_id: int):
  apartment = create_apartment(db, user_id)

  for event in events:
    name_of_reservation = event.name
    start_date= event.begin.datetime
    end_date = event.end.datetime

    start_date = confirm_datetime(start_date)
    end_date = confirm_datetime(end_date)

    # overlap = check_for_overlapping_dates(db, apartment.id, start_date, end_date)
    # if overlap:
    #   raise HTTPException(status_code=400, detail=f"Booking conflict for apartment '{apartment.name}")

    create_apartment_calendar(db, apartment.id, start_date, end_date, name_of_reservation)

  return { "message": "Calendar imported succesfully"}