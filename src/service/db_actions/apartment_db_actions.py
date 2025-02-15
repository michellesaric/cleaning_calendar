from sqlalchemy.orm import Session
from model.Apartment import Apartment
from fastapi import HTTPException
from pydantic import BaseModel

class ApartmentPyModel(BaseModel):
  name: str
  number_of_people: str

def get_apartment_by_name(db: Session, name: str):
  return db.query(Apartment).filter(Apartment.name == name).first()

def create_apartment(db: Session, apartment: ApartmentPyModel, numberOfPeople: int):
  existing_apartment = get_apartment_by_name(db, apartment.name)
  if existing_apartment:
    raise HTTPException(status_code=400, detail="Aparment name already taken")

  new_apartment = Apartment(name=apartment.name, number_of_people=numberOfPeople)
  db.add(new_apartment)
  db.commit()
  db.refresh(new_apartment)

  return new_apartment
