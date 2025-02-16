import requests
from fastapi import HTTPException
from ics import Calendar

def get_ics_from_url(url: str) -> Calendar:
  response = requests.get(url)

  if response.status_code != 200:
    raise HTTPException(status_code=400, detail="Failed to retrieve content from the URL")
  
  content_type = response.headers.get("Content-Type", "")
  if "text/calendar" not in content_type and "application/ics" not in content_type:
    raise HTTPException(status_code=400, detail="URL does not point to a valid ICS file")
  
  try:
    calendar = Calendar(response.text)
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error parsing ICS content: {str(e)}")
  
  return calendar