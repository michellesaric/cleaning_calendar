from sqlalchemy.orm import Session
from model.Apartment import Apartment
from fastapi import HTTPException
from pydantic import BaseModel

class ApartmentPyModel(BaseModel):
  name: str
  number_of_people: str

def get_apartment_by_name(db: Session, name: str):
  return db.query(Apartment).filter(Apartment.name == name).first()

def create_apartment(db: Session, number_of_people: int):
  last_apartment = db.query(Apartment).order_by(Apartment.id.desc()).first()
  new_apartment_id = (last_apartment.id + 1) if last_apartment else 1
  new_apartment_name = f"A{new_apartment_id}"

  new_apartment = Apartment(name=new_apartment_name, number_of_people=number_of_people)
  db.add(new_apartment)
  db.commit()
  db.refresh(new_apartment)

  return new_apartment
