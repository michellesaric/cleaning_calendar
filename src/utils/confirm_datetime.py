import datetime

def confirm_datetime(date):
  if not isinstance(date, datetime.datetime):
    return datetime.datetime.combine(date, datetime.datetime.min.time())
  else:
    return date