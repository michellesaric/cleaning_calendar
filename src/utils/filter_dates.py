def filter_dates(apartments, cleaning_dates):
  for apartment_name, apartment_data in apartments.items():
    valid_cleaning_dates = []

    for cleaning_date in cleaning_dates:
      is_valid = True

      for reservation in apartment_data["reservations"]:
        if reservation["start_date"] < cleaning_date < reservation["end_date"]:
          is_valid = False
          break

      if is_valid:
        valid_cleaning_dates.append(cleaning_date)
    
    valid_cleaning_dates_no_extra_cleanings = []
    for reservation in apartment_data["reservations"]:
      counter_of_cleanings = 0
      valid_cleaning_index = 0
      while(valid_cleaning_dates[valid_cleaning_index] < reservation["end_date"]):
        valid_cleaning_index +=1

      if counter_of_cleanings == 0:
        valid_cleaning_dates_no_extra_cleanings.append(valid_cleaning_dates[valid_cleaning_index])
        counter_of_cleanings +=1
    
    apartment_data["cleaning_dates"] = sorted(valid_cleaning_dates_no_extra_cleanings)

  return apartments