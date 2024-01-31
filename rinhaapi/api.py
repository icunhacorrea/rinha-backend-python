from typing import Union
from fastapi import FastAPI, HTTPException, Response, status as st
from rinhaapi.database import (get_session,
                               create_db_and_tables)
from rinhaapi.core import (get_pessoas,
                           insert_pessoa)
from rinhaapi.models import (Pessoas)
from rinhaapi.serializers import (PessoasIn,
                                  PessoasOut)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def get_hello():
    return {"Hello World": True}

@app.get("/pessoas", status_code=200)
async def return_all_pessoas(response: Response):
    pessoas = get_pessoas()
    return pessoas

@app.post("/pessoas", response_model=PessoasOut, status_code=201)
async def post_pessoa(pessoas_in: PessoasIn):
    pessoa = Pessoas(**pessoas_in.dict())
    pessoa = insert_pessoa(pessoa)

    if not pessoa:
        return HTTPException(detail="Err on trying add pessoa",
                             status_code=st.HTTP_400_BAD_REQUEST)

    return pessoa

