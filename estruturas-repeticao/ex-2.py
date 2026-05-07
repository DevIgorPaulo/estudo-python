#2) Crie um programa no qual o usuário informe o código do cargo de um funcionário (ver
#tabela abaixo) e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma
#condição de parada (por exemplo, código do cargo igual a zero). Ao fim, o programa deve
#informar a média salarial dos nutricionistas.

totalSalarioNutri = 0
qtdNutris = 0

while True:
    codigoCargo = int(input("Informe o codigo do cargo (ou digite 0 para sair): "))

    if(codigoCargo == 0):
        break

    salario = float(input("Informe o sálario: "))

    if(codigoCargo == 2):
        qtdNutris += 1
        totalSalarioNutri += salario

if(qtdNutris > 0):
    mediaNutri = totalSalarioNutri / qtdNutris
    print(f"A média sálarial dos nutricionistas é {mediaNutri}")
else:
    print("Nenhum nutricionista informado")
