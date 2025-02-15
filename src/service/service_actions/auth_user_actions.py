from fastapi import HTTPException
from sqlalchemy.orm import Session

from service.db_actions.user_db_actions import create_user, get_user_by_username
from utils.hash_password import hash_password
from utils.verify_password import verify_password
from utils.create_access_token import create_access_token

def register_new_user(db: Session, user):
  hashed_password = hash_password(user.password)
  create_user(db, user, hashed_password)
  login_existing_user(db, user)

def login_existing_user(db: Session, user):
  db_user = get_user_by_username(db, user.username)
  if not db_user or not verify_password(user.password, db_user.password):
    raise HTTPException(status_code=401, detail="Invalid credentials")

  access_token = create_access_token(data={"sub": db_user.username, "id": db_user.id})

  return {"access_token": access_token, "token_type": "bearer"}
