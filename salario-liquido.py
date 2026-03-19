#valor da hora, número de horas trabalhadas no mês e percentual de desconto do INSS
#Em primeiro lugar, deve-se estabelecer qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.
valorHora = float(input("Informe o valor da hora: "))
horasTrabalhadas = float(input("Informe o número de horas trabalhadas: "))
percentualDesconto = float(input("Informe o percentual de desconto do INSS: "))

salarioBruto = valorHora * horasTrabalhadas
salarioLiquido = salarioBruto * (1 - (percentualDesconto / 100))

print(f"Seu sálario bruto é: {salarioBruto}")
print(f"Seu sálario liquid é: {salarioLiquido}")



