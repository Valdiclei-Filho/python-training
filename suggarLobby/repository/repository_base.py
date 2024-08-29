from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity.Entities import Base

db_url= 'mysql://root:root@localhost:3306/python_training'
engine= create_engine(db_url)
        
def create_tables():
    try:  
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f'Erro ao criar as tabelas: {e}')

    try:
        with engine.connect():
            print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

def create_session():
    Session= sessionmaker(bind=engine)
    session= Session();
    return session;
