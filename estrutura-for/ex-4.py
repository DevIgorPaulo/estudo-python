# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas
# em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o
# valor -273°C.
encerramento = -273

celsius = 0
soma = 0
c = 0

while celsius != encerramento:
    celsius = float(input("Informe a temperatura em Celsius: "))

    if(celsius != encerramento):
        soma += celsius
        c += 1

if(c > 1):
    media = soma / c
    print(f"A média das temperaturas é {media:.2f}")
else:
    print("Informe no mínimo duas temperaturas")
