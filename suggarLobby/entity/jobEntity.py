from datetime import datetime, timedelta
from typing import List
import acompanhanteEntity as acompanhante
import clienteEntity as cliente

class JobTypeEntity:
    def __init__(self, id: int, type: str, valor : float):
        self.id = id;
        self.type = type;
        self.valor = valor;
        
class JobEntity:
    def __init__(self, 
                 id: int, 
                 valor: float, 
                 inicio: datetime, 
                 fim: datetime, 
                 jobs: List[JobTypeEntity], 
                 acompanhante: acompanhante, 
                 cliente: cliente):
        self.id = id;
        self.valor = valor;
        self.inicio = inicio;
        self.fim = fim;
        self.jobs = jobs;
        self.acompanhante = acompanhante;
        self.cliente = cliente;

    def calcularDuracao(self) -> timedelta:
        return self.fim - self.inicio;
    