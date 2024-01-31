from sqlalchemy.exc import NoResultFound
from sqlmodel import select

from rinhaapi.models import Pessoas
from rinhaapi.database import get_session

def get_pessoas():
    with get_session() as session:
        query = select(Pessoas)
        res = session.exec(query)
        return res.all() 

def get_pessoa_by_apelido(apelido: str):
    try:
        with get_session() as session:
            query = select(Pessoas).where(Pessoas.apelido == apelido)
            res = session.exec(query)
            pessoa = res.one()
            session.close()
            return pessoa
    except Exception as err:
        print(f"Err on get pessoa by apelido. {err}")
        return None

def insert_pessoa(pessoa: Pessoas):
    try:
        with get_session() as session:
            print(pessoa)
            session.add(pessoa)
            session.commit()
            session.refresh(pessoa)
            session.close()
            return pessoa
    except Exception as err:
        print(f"Err on trying insert pessoa: {err}")
        return None
