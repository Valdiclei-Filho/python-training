import keyboard as k

#region Utils
def getInputAsInt():
    try:
        return int(input());
    except ValueError:
        print(msgValorInvalidoNumero);

def getInputAsFloat():
    try:
        return float(input());
    except ValueError:
        print(msgValorInvalidoNumero);

def getInputAsStr():
    try:
        return str(input());
    except ValueError:
        print(msgValorInvalidoStr);
#endregion

print('Calculadora');
print('=======================');

msgValorInvalidoNumero = 'Valor informado inválido, Informe um número.';
msgValorInvalidoStr = 'Valor informado inválido, Informe um texto.';
resultado = 'Resultado: ';
rodando = True

while rodando:
    print('Pressione ESC para encerrar')

    if k.is_pressed('esc'):
        rodando = False;
        continue
    
    print('Informe o primeiro número:')
    n1 = getInputAsFloat();

    print('Informe o segundo número:')
    n2 = getInputAsFloat();

    print('Selecione a operação matemática:');
    print('1 - Subtração');
    print('2 - Divisão');
    print('3 - Multiplicação');
    print('4 - Adição');

    operacao = getInputAsInt();

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
