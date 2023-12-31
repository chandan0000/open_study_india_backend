# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlmodel import sessionmaker
# from sqlmodel import SQLModel
from sqlmodel import SQLModel, create_engine, Session
from .config import settings


SQLALCHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base=declarative_base()
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)




#     from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from psycopg2.extras import RealDictCursor

# from .config import settings

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()