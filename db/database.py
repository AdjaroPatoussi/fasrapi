from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/test"

# # postgres://postgres:password@localhost:5432/dbname postgres zone


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db  = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        