# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  PostgreSQL  en local
SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin123@localhost:5433/gptdb"

#  PostgreSQL  en deploiement avec Docker Compose
# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin123@db-service:5432/gptdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()