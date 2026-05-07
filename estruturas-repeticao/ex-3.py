# 3) Com base na tabela salarial da questão anterior, crie um pro grama que informe a
# quantidade de médicos com salários superiores a R$ 4.500,00.

qtdMedicos = 0

while True:
    codigoCargo = int(input("Informe o codigo do cargo (ou digite 0 para sair): "))

    if(codigoCargo == 0):
        break

    salario = float(input("Informe o sálario: "))

    if(codigoCargo == 3 and salario > 4500):
        qtdMedicos += 1

print(f"{qtdMedicos} médicos têm sálario superior a R$ 4.500,00")
