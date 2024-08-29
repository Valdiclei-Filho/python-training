from repository import repository_base, acompanhante_repository
from entity.Entities import AcompanhanteEntity
import datetime

def main():
    print('Iniciando a aplicação...')
    
    print('Criando tabelas')
    repository_base.create_tables();
    print('Tabelas criadas')
    
    print('Aplicação está rodando!')
    

if __name__ == "__main__":
    main()