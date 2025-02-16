import os
from dotenv import load_dotenv
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def decode_access_token(token) -> dict:
  return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])