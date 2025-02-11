import os
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.User import Base

db_user: str = "postgres"
db_port: int = 5432
db_host: str = "localhost"
db_password: str = "nesnikadpogodit"
db_name: str = "cleaning-schedule"

uri: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(uri)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

db_session = SessionLocal()

try:
  connection = engine.connect()
  connection.close()
  print("✅ Connected to the database!")
except Exception as e:
  print(f"❌ Error: {str(e)}")
