from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# this two lines are necessary for PostgreSQL
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# this two lines are necessary for sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
