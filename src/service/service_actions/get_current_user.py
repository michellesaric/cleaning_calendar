from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from jose import jwt, JWTError

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def get_current_user(token: str = Security(api_key_header)):
  if not token.startswith("Bearer "):
    raise HTTPException(status_code=403, detail="Invalid token format")
    
  token = token.split("Bearer ")[1]
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
      raise HTTPException(status_code=401, detail="Invalid token")
  except JWTError:
    raise HTTPException(status_code=401, detail="Could not validate credentials")
    
  return {"username": username}