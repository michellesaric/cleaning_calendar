from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from data.database import get_db
from service.db_actions.user_db_actions import UserPyModel
from service.db_actions.apartment_calendar_db_actions import get_all_calendars, get_calendar_by_id
from service.service_actions.get_current_user import get_current_user
from service.service_actions.import_calendar_actions import import_calendar_from_ics_file, import_calendar_from_url
from service.service_actions.export_calendar_actions import export_all_calendars_and_cleaning_schedule, export_reservations_and_cleaning_dates_by_id

router = APIRouter()

@router.post("/import-calendar")
async def import_calendar(file: UploadFile = File(...),db: Session = Depends(get_db), current_user: UserPyModel = Depends(get_current_user)):
    return await import_calendar_from_ics_file(file, db, current_user.id)

@router.post("/import-from-url")
async def import_calendar_url(url:str, db: Session = Depends(get_db), current_user: UserPyModel = Depends(get_current_user)):
    return await import_calendar_from_url(url, db, current_user.id)

@router.get("/export/{calendarId}")
def export_calendar_by_id(calendarId, db: Session = Depends(get_db), current_user: UserPyModel = Depends(get_current_user)):
    return export_reservations_and_cleaning_dates_by_id(db, current_user.id, calendarId)

@router.get("/calendars")
def get_calendars(db: Session = Depends(get_db), current_user: UserPyModel = Depends(get_current_user)):
    return export_all_calendars_and_cleaning_schedule(db, current_user.id)
