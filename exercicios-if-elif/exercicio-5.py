nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

if not (0 <= nota1 <= 10):
    print("Primeira nota inválida!")
    exit()

if not (0 <= nota2 <= 10):
    print("Segunda nota inválida!")
    exit()

if 9 <= media <= 10:
    conceito = 'A'
    resultado = 'Aprovado'
elif 7.5 <= media < 9:
    conceito = 'B'
    resultado = 'Aprovado'
elif 6 <= media < 7.5:
    conceito = 'C'
    resultado = 'Aprovado'
elif 4 <= media < 6:
    conceito = 'D'
    resultado = 'Reprovado'
else:
    conceito = 'E'
    resultado = 'Reprovado'

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)
print("Conceito:", conceito)
print("Resultado:", resultado)