import os
import logging
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
url_object = URL.create(
    drivername='mysql+pymysql',
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv("DB_HOST"),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_SCHEMA'),
)
engine = create_engine(
    url=url_object, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
