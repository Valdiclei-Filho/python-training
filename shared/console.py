from datetime import datetime
msgValorInvalidoNumero = 'Valor informado inválido, Informe um número.';
msgValorInvalidoStr = 'Valor informado inválido, Informe um texto.';
msgDataInvalida = "Data informada inválida."

#region Utils
def getInputAsInt(msgValorInvalidoNumero = msgValorInvalidoNumero):
    try:
        return int(input());
    except ValueError:
        print(msgValorInvalidoNumero);

def getInputAsFloat(msgValorInvalidoNumero = msgValorInvalidoNumero):
    try:
        return float(input());
    except ValueError:
        print(msgValorInvalidoNumero);

def getInputAsStr(msgValorInvalidoStr = msgValorInvalidoStr):
    try:
        return str(input());
    except ValueError:
        print(msgValorInvalidoStr);
        
def getInputAsDate(msgDataInvalida = msgDataInvalida):
    try:
        return datetime.strptime(input(), '%Y-%m-%d').date()
    except ValueError:
        print(msgDataInvalida)

def breakLine():
    print('')
#endregion