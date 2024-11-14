from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'postgresql://admin:1234@localhost:5437/missions_db'

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)
