from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from data.database import get_db
from service.service_actions.get_current_user import get_current_user
from service.db_actions.apartment_calendar_db_actions import get_all_calendars, get_calendar_by_id
from service.service_actions.import_calendar_actions import import_calendar_from_ics_file, import_calendar_from_url

router = APIRouter()

@router.post("/import-calendar", dependencies=[Depends(get_current_user)])
async def import_calendar(file: UploadFile = File(...),db: Session = Depends(get_db)):
    return await import_calendar_from_ics_file(file, db)

@router.post("/import-from-url", dependencies=[Depends(get_current_user)])
async def import_calendar_url(url:str, db: Session = Depends(get_db)):
    return await import_calendar_from_url(url, db)

@router.get("/export/{calendarId}", dependencies=[Depends(get_current_user)])
def export_calendar_by_id(calendarId, db: Session = Depends(get_db)):
    return get_calendar_by_id(db, calendarId)

@router.get("/calendars", dependencies=[Depends(get_current_user)])
def get_calendars(db: Session = Depends(get_db)):
    return get_all_calendars(db)
