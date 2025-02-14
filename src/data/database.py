from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

db_user: str = "postgres"
db_port: int = 5432
db_host: str = "localhost"
db_password: str = "nesnikadpogodit"
db_name: str = "cleaning-schedule"

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
