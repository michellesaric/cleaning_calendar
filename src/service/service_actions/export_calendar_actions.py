from sqlalchemy.orm import Session
from collections import defaultdict
from service.db_actions.apartment_calendar_db_actions import get_all_calendars
from service.db_actions.apartment_db_actions import get_apartment_by_id
from utils.filter_dates import filter_dates

def export_all_calendars_and_cleaning_schedule(db: Session, user_id: int):
  reservations = get_all_calendars(db, user_id)
  apartments = defaultdict(lambda: {"reservations": [], "cleaning_dates": []})
  all_start_dates = []
  all_end_dates = []
  cleaning_dates = []
  start_date_index = 0

  for reservation in reservations:
    apartment_name = reservation["name"]
    apartments[apartment_name]["reservations"].append({
      "start_date": reservation["start_date"],
      "end_date": reservation["end_date"],
      "name_of_reservation": reservation["name_of_reservation"]
  })
    all_start_dates.append(reservation["start_date"])
    all_end_dates.append(reservation["end_date"])

  all_sorted_end_dates = sorted(all_end_dates)
  all_sorted_start_dates = sorted(all_start_dates)

  for i, end_date in enumerate(all_sorted_end_dates):
    while start_date_index < len(all_sorted_start_dates) and all_sorted_start_dates[start_date_index] < end_date:
      start_date_index += 1
    if start_date_index >= len(all_sorted_start_dates):
      break
    if all_sorted_end_dates[i + 1] > all_sorted_start_dates[start_date_index]:
      cleaning_dates.append(end_date)
  cleaning_dates.append(all_sorted_end_dates[-1])

  apartments = filter_dates(apartments, cleaning_dates)

  return [{"apartment_name": name, **data} for name, data in apartments.items()]

def export_reservations_and_cleaning_dates_by_id(db: Session, user_id: int, apartmentId):
  apartment_reservations = export_all_calendars_and_cleaning_schedule(db, user_id)
  apartment = get_apartment_by_id(db, apartmentId)

  for apartment_data in apartment_reservations:
    if apartment_data["apartment_name"] == apartment.name:
      return apartment_data
    return None