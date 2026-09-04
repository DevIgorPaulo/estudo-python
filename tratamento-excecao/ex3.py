numero1 = input("Digite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")

try:
    numero1 = float(numero1)
    numero2 = float(numero2)

    resultado = numero1 / numero2
except ValueError:
    print("Digite apenas numeros!")
except ZeroDivisionError:
    print("Um numero não pode ser dividido por zero!")
else:
    print(resultado)