valorEmprestimo = float(input("Informe o valor do empréstimo: "))
numeroParcelas = int(input("Informe o número de parcelas: "))
salarioSolicitante = float(input("Informe o sálario do solicitante: "))

valorParcela = valorEmprestimo / numeroParcelas
porcentagemParcela = valorParcela / salarioSolicitante * 100

if(porcentagemParcela > 30):
    print(f"O valor da parcela equivale à {porcentagemParcela} do seu sálario!")
    print("Empréstimo não foi aprovado!")
else:
    print("Empréstimo aprovado!")