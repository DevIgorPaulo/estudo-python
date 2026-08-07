def calculadora(num1, num2, operacao):
    if(operacao == '+'):
        return num1 + num2
    
    if(operacao == '-'):
        return num1 - num2
    
    if(operacao == '*'):
        return num1 * num2
    
    if(operacao == '/'):
        if(num2 == 0): return 'Operacao Invalida! Não se pode dividir um numero por 0.'
        return num1 / num2
    
    return 'Operação Inválida! Operador inválido.'

print(calculadora(4, 0, '#'))

 