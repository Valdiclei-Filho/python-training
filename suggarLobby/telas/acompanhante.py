from shared import console
from entity.Entities import AcompanhanteEntity

def cadastrar():
    print('Cadastro de acompanhante')
    console.breakLine()
    
    print('preço da hora: ')
    precoHora= console.getInputAsFloat()
    
    print('data nascimento: ')
    dataNascimento= console.getInputAsDate()
    
    print('carga horario: ')
    cargaHoraria= console.getInputAsFloat()
    
    print('nome: ')
    nome= console.getInputAsStr()
    
    acompanhante= AcompanhanteEntity()
    
    acompanhante.precoHora= precoHora;
    acompanhante.dataNascimento= dataNascimento;
    acompanhante.cargaHoraria= cargaHoraria;
    acompanhante.nome= nome;