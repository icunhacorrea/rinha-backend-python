import asyncio
import uuid
from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, HTTPException, Query, status as st, BackgroundTasks
from rinhaapi.database import (create_db_and_tables)
from rinhaapi.core import (search_pessoa_by_id,
                           insert_pessoa,
                           search_pessoas_by_term,
                           count_pessoas)
from rinhaapi.models import (Pessoas)
from rinhaapi.serializers import (PessoasIn,
                                  PessoasOut)
from rinhaapi.worker import Worker
from rinhaapi.queue import pessoas_queue


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    worker = Worker()
    task = asyncio.create_task(worker.run())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

@app.post("/pessoas", status_code=201)
async def post_pessoa(pessoas_in: PessoasIn,
                      background_tasks: BackgroundTasks):
    pessoa = Pessoas(**pessoas_in.dict())
    pessoa = insert_pessoa(pessoa)

    _uuid = str(uuid.uuid4())
    pessoa.uuid = _uuid

    await pessoas_queue.put(pessoa.model_dump())

    if not pessoa:
        return HTTPException(detail="Err on trying add pessoa",
                             status_code=st.HTTP_404_NOT_FOUND)

@app.get("/pessoas/{id}", response_model=PessoasOut, status_code=200)
async def get_pessoa(id: str):
    pessoa = search_pessoa_by_id(id)

    if not pessoa:
        return HTTPException(detail="Err on trying add pessoa",
                             status_code=st.HTTP_404_NOT_FOUND)

    return pessoa

@app.get("/pessoas", response_model=List[Pessoas], status_code=200)
async def get_pessoas_with_term(term: str = Query(..., alias="term")):
    return search_pessoas_by_term(term)

@app.get("/contagem-pessoas", status_code=200)
async def check_pessoas_count():
    count = count_pessoas()
    return {"count": count}
