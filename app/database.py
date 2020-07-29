from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()