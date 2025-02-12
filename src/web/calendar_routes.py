from fastapi import APIRouter

router = APIRouter()

@router.get("/import-calendar")
def import_calendar():
  return "So apperantly, here I can import a calendar into my app in .ics format...interesting"

@router.get("/import-from-url")
def import_calendar_from_url():
  return "Here I also import calendar, but this time from a url"

@router.get("/export/{calendarId}")
def export_calendar_by_id(calendarId):
  return f"Finally, an actual get method, here we get the calendar with id {calendarId}"

@router.get("/calendars")
def get_all_calendars():
  return "So, I return all calendars here. Cool. (FastAPI already returns everything in JSON. We love FastAPI)"