import os
from dotenv import load_dotenv
import datetime
from datetime import timezone, timedelta
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
  to_encode = data.copy()
  to_encode.update({"exp": datetime.datetime.now(timezone.utc) + expires_delta})

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)