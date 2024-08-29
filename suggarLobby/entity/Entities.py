from datetime import datetime, timedelta
from sqlalchemy import ForeignKey, String, Integer, Column, Numeric, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AcompanhanteEntity(Base):
    __tablename__ = 'acompanhantes'
    
    id = Column('Id', Integer, primary_key=True, autoincrement=True, unique=True)
    precoHora = Column('PrecoHora', Numeric(5, 2), nullable=False)
    dataNascimento = Column('DataNascimento', DateTime, nullable=False)
    cargaHoraria = Column('CargaHoraria', Numeric(5, 2), nullable=False)
    nome = Column('Nome', String(45), nullable=False)
    dataCadastro = Column('DataCadastro', DateTime, nullable=False, default=datetime.now())
    
    jobs = relationship('JobEntity', back_populates='acompanhante')

class ClienteEntity(Base):
    __tablename__ = 'clientes'
    
    id = Column('Id', Integer, primary_key=True, autoincrement=True, unique=True)
    nome = Column('Nome', String(45), nullable=False)
    dataNascimento = Column('DataNascimento', DateTime, nullable=False)
    dataCadastro = Column('DataCadastro', DateTime, nullable=False, default=datetime.now())
    
    jobs = relationship('JobEntity', back_populates='cliente')

class JobTipoEntity(Base):
    __tablename__ = 'job_tipos'
    
    id = Column('Id', Integer, primary_key=True, autoincrement=True, unique=True)
    nome = Column('Nome', String(45), nullable=False, unique=True)
    valor = Column('Valor', Numeric(5, 2), nullable=False)

class JobEntity(Base):
    __tablename__ = 'jobs'
    
    id = Column('Id', Integer, primary_key=True, autoincrement=True, unique=True)
    valorFinal = Column('ValorFinal', Numeric(5, 2), nullable=False)
    inicio = Column('Inicio', DateTime, nullable=False)
    fim = Column('Fim', DateTime, nullable=False)
    clienteId = Column('ClienteId', Integer, ForeignKey('clientes.Id'), nullable=False)
    acompanhanteId = Column('AcompanhanteId', Integer, ForeignKey('acompanhantes.Id'), nullable=False)
    
    cliente = relationship('ClienteEntity', back_populates='jobs')
    acompanhante = relationship('AcompanhanteEntity', back_populates='jobs')

    def calcularDuracao(self) -> timedelta:
        return self.fim - self.inicio
    
class JobRealizadoEntity(Base):
    __tablename__= 'jobs_realizados'
    
    id = Column('Id', Integer, primary_key=True, autoincrement=True, unique=True)
    jobId= Column('JobId', Integer, ForeignKey('jobs.Id'))
    jobTipoId= Column('JobTipoId', Integer, ForeignKey('job_tipos.Id'))
    