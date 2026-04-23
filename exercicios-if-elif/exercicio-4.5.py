dia = int(input("Informe o dia: "))
diasSemana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']

if(dia >= 1 and dia <= 7):
    print("Este dia é: ", diasSemana[dia-1])
else:
    print("Valor inválido!")