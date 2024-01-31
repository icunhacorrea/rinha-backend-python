import warnings

from sqlmodel import (SQLModel,
                      Session,
                      create_engine)
from sqlmodel.sql.expression import (Select,
                                     SelectOfScalar)
from sqlalchemy.exc import (SAWarning)

from rinhaapi import models

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

database_url = "mysql+mysqlconnector://admin:pass@localhost:3306/rinhadb"

engine = create_engine(database_url,
                       echo=True)

def create_db_and_tables():
    models.SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

