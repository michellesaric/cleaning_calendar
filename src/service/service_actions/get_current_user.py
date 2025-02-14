from fastapi import Security, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from data.database import get_db  # Import your DB session
from service.db_actions.user_db_actions import get_user_by_username
from utils.decode_access_token import decode_access_token

security = HTTPBearer()

def get_current_user(
  credentials: HTTPAuthorizationCredentials = Security(security),
  db: Session = Depends(get_db)
):
  token = credentials.credentials

  try:
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    if username is None:
      raise HTTPException(status_code=401, detail="Invalid token")
  except Exception:
    raise HTTPException(status_code=401, detail="Could not validate credentials")

  user = get_user_by_username(db, username)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  return user
