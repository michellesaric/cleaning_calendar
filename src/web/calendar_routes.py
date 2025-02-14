from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from service.service_actions.get_current_user import get_current_user
router = APIRouter()

@router.get("/import-calendar")
def import_calendar(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
  return {"message": "Import calendar from ics", "user": current_user.username}

@router.get("/import-from-url")
def import_calendar_from_url(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
  return {"message": "Import calendar from url", "user": current_user.username}

@router.get("/export/{calendarId}")
def export_calendar_by_id(calendarId, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
  return {"message": "Specific calendar", "user": current_user.username, "calendarId": calendarId}

@router.get("/calendars")
def get_all_calendars(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
  return {"message": "All calendars", "user": current_user.username}