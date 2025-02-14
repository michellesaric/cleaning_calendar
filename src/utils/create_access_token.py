from jose import jwt
import datetime
from datetime import timezone, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=10)):
  to_encode = data.copy()
  to_encode.update({"exp": datetime.datetime.now(timezone.utc) + expires_delta})

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)