from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity.Entities import Base

def create_tables():
    try:
        db_url = 'mysql://root:root@localhost:3306/harmonic'
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        print(f'Erro ao criar as tabelas: {e}')

    try:
        with engine.connect():
            print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
