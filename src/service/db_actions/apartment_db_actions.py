from sqlalchemy.orm import Session
from model.Apartment import Apartment
from pydantic import BaseModel

class ApartmentPyModel(BaseModel):
  name: str
  user_id: int

def get_apartment_by_id(db: Session, id: int):
  return db.query(Apartment).filter(Apartment.id == id).first()

def create_apartment(db: Session, user_id: int):
  last_apartment = db.query(Apartment).order_by(Apartment.id.desc()).first()
  new_apartment_id = (last_apartment.id + 1) if last_apartment else 1
  new_apartment_name = f"A{new_apartment_id}"

  new_apartment = Apartment(name=new_apartment_name, user_id=user_id)
  db.add(new_apartment)
  db.commit()
  db.refresh(new_apartment)

  return new_apartment
