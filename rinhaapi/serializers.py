from uuid import UUID
from datetime import date
from typing import List, Union 
from fastapi import HTTPException, status as st
from pydantic import (BaseModel,
                      field_validator)

from rinhaapi.core import get_pessoa_by_apelido

class PessoasIn(BaseModel):
    apelido: str
    nome: str
    nascimento: date
    stack: Union[List[str], None] = None

    @field_validator("apelido")
    def validate_apelido(cls, v):
        if get_pessoa_by_apelido(v):
            raise HTTPException(detail="Duplicated apelido",
                                status_code=st.HTTP_422_UNPROCESSABLE_ENTITY)
        return v

    @field_validator("nome")
    def validate_nome(cls, v):
        if isinstance(v, int):
            raise HTTPException(detail="Nome should be str.",
                                status_code=st.HTTP_400_BAD_REQUEST)
        return v

    @field_validator("stack")
    def validate_stack(cls, v):
        for val in v:
            if isinstance(val, int):
                raise HTTPException(detail="Stack should be arr of str",
                                    status_code=st.HTTP_400_BAD_REQUEST)
        return v

class PessoasOut(BaseModel):
    uuid: UUID
    apelido: str
    nascimento: date
    stack: Union[List[str], None] = None
