import keyboard as k
from shared import console

print('Calculadora');
print('=======================');

resultado = 'Resultado: ';
rodando = True

while rodando:
    print('Pressione ESC para encerrar')

    if k.is_pressed('esc'):
        rodando = False;
        continue
    
    print('Informe o primeiro número:')
    n1 = console.getInputAsFloat();

    print('Informe o segundo número:')
    n2 = console.getInputAsFloat();

    print('Selecione a operação matemática:');
    print('1 - Subtração');
    print('2 - Divisão');
    print('3 - Multiplicação');
    print('4 - Adição');

    operacao = console.getInputAsInt();

    if operacao == 1:
        print(f'{resultado} {n1 - n2}')
    elif operacao == 2:
        try:
            print(f'{resultado} {n1 / n2}')
        except ZeroDivisionError:
            print('Não é possível dividir por zero')
    elif operacao == 3:
        print(f'{resultado} {n1 * n2}')
    elif operacao == 4:
        print(f'{resultado} {n1 + n2}')
    else:
        print('Operação inválida. Selecione uma opção de 1 a 4.')

print('Calculadora encerrada.')
