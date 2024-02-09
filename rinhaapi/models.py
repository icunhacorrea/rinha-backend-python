import uuid
from uuid import (UUID)
from datetime import date
from typing import List, Optional
from sqlmodel import (JSON, Column, SQLModel,
                      Field)

from rinhaapi.database import SQLModel

def generate_uuid():
    return str(uuid4())

class Pessoas(SQLModel, table=True):
    uuid: Optional[UUID] = Field(default_factory=uuid.uuid4,
                                 primary_key=True,
                                 index=True,
                                 nullable=False)
    apelido: str = Field(unique=True,
                         nullable=False)
    nome: str = Field(nullable=False)
    nascimento: date
    stack: List[str] = Field(sa_column=Column(JSON),
                             default=None)

    class Config:
        arbitrary_types_allowed = True
