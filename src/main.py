import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def top():
  return "This is the top"

@app.get("/register")
def register_user():
  return "Time to register a user(not supposed to be a get method)"

@app.get("/login")
def login_user():
  return "This isn't supposted to be a get method, but it's okay for now, login the user"

@app.get("/import-calendar")
def import_calendar():
  return "So apperantly, here I can import a calendar into my app in .ics format...interesting"

@app.get("/import-from-url")
def import_calendar_from_url():
  return "Here I also import calendar, but this time from a url"

@app.get("/export/{calendarId}")
def export_calendar_by_id(calendarId):
  return f"Finally, an actual get method, here we get the calendar with id {calendarId}"

@app.get("/calendars")
def get_all_calendars():
  return "So, I return all calendars here. Cool. (FastAPI already returns everything in JSON. We love FastAPI)"

if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)