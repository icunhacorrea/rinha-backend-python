from uuid import UUID
from datetime import date
from typing import List, Optional
from fastapi import HTTPException, status as st
from pydantic import (BaseModel,
                      field_validator)

from rinhaapi.core import get_pessoa_by_apelido

class PessoasIn(BaseModel):
    apelido: str
    nascimento: date
    stack: Optional[List[str]] = None

    @field_validator("apelido")
    def validate_apelido(cls, v):
        if get_pessoa_by_apelido(v):
            raise HTTPException(detail="Duplicated apelido",
                                status_code=st.HTTP_422_UNPROCESSABLE_ENTITY)
        return v

class PessoasOut(BaseModel):
    uuid: UUID
    apelido: str
    nascimento: date
    stack: List[str] = None
