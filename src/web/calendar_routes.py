from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from service.service_actions.get_current_user import get_current_user
from service.db_actions.apartment_calendar_db_actions import get_all_calendars, get_calendar_by_id

router = APIRouter()

@router.get("/import-calendar", dependencies=[Depends(get_current_user)])
def import_calendar(db: Session = Depends(get_db)):
    return {"message": "Import calendar from ics"}

@router.get("/import-from-url", dependencies=[Depends(get_current_user)])
def import_calendar_from_url(db: Session = Depends(get_db)):
    return {"message": "Import calendar from url"}

@router.get("/export/{calendarId}", dependencies=[Depends(get_current_user)])
def export_calendar_by_id(calendarId, db: Session = Depends(get_db)):
    return get_calendar_by_id(db, calendarId)

@router.get("/calendars", dependencies=[Depends(get_current_user)])
def get_calendars(db: Session = Depends(get_db)):
    return get_all_calendars(db)
