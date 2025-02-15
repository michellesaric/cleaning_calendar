import datetime
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from ics import Calendar

from service.db_actions.apartment_calendar_db_actions import check_for_overlapping_dates, create_apartment_calendar
from service.db_actions.apartment_db_actions import create_apartment

async def import_calendar_from_ics_file(file: UploadFile, db: Session):
  try:
    content = await file.read()
    calendar = Calendar(content.decode("utf-8"))

    apartment = create_apartment(db, number_of_people=3)

    for event in calendar.events:
      name_of_reservation = event.name
      start_date= event.begin.datetime
      end_date = event.end.datetime

      if not isinstance(start_date, datetime.datetime) is False:
        start_date = datetime.datetime.combine(start_date, datetime.datetime.min.time())
      if not isinstance(end_date, datetime.datetime) is False:
        end_date = datetime.datetime.combine(end_date, datetime.datetime.min.time())

      overlap = check_for_overlapping_dates(db, apartment.id, start_date, end_date)
      if overlap:
        raise HTTPException(status_code=400, detail=f"Booking conflict for apartment '{apartment.name}")

      return create_apartment_calendar(db, apartment.id, start_date, end_date, name_of_reservation)

  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error processing ICS file: {str(e)}")