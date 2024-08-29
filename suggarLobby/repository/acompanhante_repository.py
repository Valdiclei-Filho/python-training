from entity.Entities import AcompanhanteEntity
from repository import repository_base  as repo

def add(acompanhante: AcompanhanteEntity):
    session= repo.create_session()
    session.add(acompanhante)
    session.commit()

def delete(acompanhante: AcompanhanteEntity):
    session= repo.create_session()
    session.delete(acompanhante)
    session.commit()

def update(id: int):
    session= repo.create_session()
    session.