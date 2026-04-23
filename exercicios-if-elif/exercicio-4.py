salario = float(input("Informe seu sálario: "))
percentual = 0
valorValido = False

while valorValido == False:      
    if(salario <= 0):
        salario = float(input("Informe um valor válido: "))        
    else:
        valorValido = True
    
if (salario <= 280):
    percentual = 20
elif (salario <= 720):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

valorAumento = salario * percentual / 100
salarioNovo = salario + valorAumento

print("Salário antigo: ", salario)
print("Percentual do aumento: ", percentual)
print("Valor do aumento: ", valorAumento)
print("Novo salário: ", salarioNovo)
