from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from service.service_actions.auth_user_actions import register_new_user, login_existing_user
from service.db_actions.user_db_actions import UserPyModel

router = APIRouter()

@router.post("/register")
def register_user(user: UserPyModel, db: Session = Depends(get_db)):
  return register_new_user(db, user)

@router.post("/login")
def login_user(user: UserPyModel, db: Session = Depends(get_db)):
  return login_existing_user(db, user)
