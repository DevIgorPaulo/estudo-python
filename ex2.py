notas = []
contador = 1

while contador <= 6:
    try:

        nota = float(input(f"Informe a {contador}º nota: "))

        if nota < 0 or nota > 10:
            print("A nota deve ser maior que 0 e menor que 10")
            continue

        notas.append(nota)
        contador += 1
    except ValueError:
        print("Digite apenas números")

print(notas)