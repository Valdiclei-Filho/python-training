from enum import Enum

class TipoPessoa(Enum):
    ACOMPANHANTE = "Acompanhante"
    CLIENTE = "Cliente"

    def __str__(self):
        return self.value