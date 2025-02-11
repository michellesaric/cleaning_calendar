from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user: str = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = 'nesnikadpogodit'

uri: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/cleaning-schedule'

engine = create_engine(uri)

session = sessionmaker(
  bind=engine,
  autoflush=True
)

db_session = session()

try:
  connection = engine.connect()
  connection.close()
  print('ping, Connected')
except Exception as e:
  print(f'Error: {str(e)}')