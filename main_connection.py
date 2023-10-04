from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from models.models import User,Address 

def get_engine(user, password,host=None,port=None, dbname=None):
    # url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}" 
    # print('url:',url)
    # if not database_exists(url):
    #     create_database(url)
    engine = create_engine('postgresql+psycopg2://postgres:123456789a@localhost:5432/postgres',echo=False)
    return engine

engine = get_engine('postgres', '123456789a@', 'localhost', 5432, 'postgres')

with engine.connect() as session:
    print(session)
    sql = 'select * from user_account'
    stmt = session.execute(text(sql)).scalar_one()

    for user in stmt:
        print(user)

