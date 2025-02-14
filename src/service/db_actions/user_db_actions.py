from sqlalchemy.orm import Session
from model.User import User
from fastapi import HTTPException
from pydantic import BaseModel

class UserPyModel(BaseModel):
    username: str
    password: str

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserPyModel, hashed_password: str):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
