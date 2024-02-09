from sqlmodel import select, or_, func

from rinhaapi.models import Pessoas
from rinhaapi.database import get_session

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
            session.add(pessoa)
            session.commit()
            session.refresh(pessoa)
            session.close()
            return pessoa
    except Exception as err:
        print(f"Err on trying insert pessoa: {err}")
        return None

def search_pessoa_by_id(id: str):
    try:
        with get_session() as session:
            query = select(Pessoas).where(Pessoas.uuid == id)
            res = session.exec(query)
            pessoa = res.one()
            session.close()
            return pessoa
    except Exception as err:
        print(f"Err on get pessoa by id. {err}")
        return None

def search_pessoas_by_term(term: str):
    try:
        with get_session() as session:
            query = select(Pessoas).where(
                    or_(Pessoas.stack.contains([term]),
                        Pessoas.nome.contains(term),
                        Pessoas.apelido.contains(term))).limit(50)
            res = session.exec(query)
            pessoas = res.all()
            session.close()
            print(pessoas)
            return pessoas
    except Exception as err:
        print(f"Err on get pessoa by term. {err}")
        return None

def count_pessoas():
    try:
        with get_session() as session:
            query = select(func.count(Pessoas.uuid))
            res = session.exec(query)
            session.close()
            return res.one()
    except Exception as err:
        print(f"Err on count pessoas.")
        raise err
