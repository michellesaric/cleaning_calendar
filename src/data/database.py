import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

db_user: str = os.getenv("DB_USER")
db_port: int = os.getenv("DB_PORT")
db_host: str = os.getenv("DB_HOST")
db_password: str = os.getenv("DB_PASSWORD")
db_name: str = os.getenv("DB_NAME")

uri: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(uri)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
  db: Session = SessionLocal()
  try:
    yield db
  except Exception as e:
    db.rollback()
    raise e
  finally:
    db.close()
