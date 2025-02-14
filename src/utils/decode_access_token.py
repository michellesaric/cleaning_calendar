from jose import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def decode_access_token(token) -> dict:
  return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])