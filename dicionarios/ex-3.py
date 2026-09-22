contador_numeros = {}

while True:
    numero = int(input("Digite o número: "))

    if(numero <= 0):
        break

    if numero in contador_numeros:
        contador_numeros[numero] += 1
    else:
        contador_numeros[numero] = 1

for numero, quantidade in contador_numeros.items():
    label = "vezes" if quantidade > 1 else "vez"
    print(f"Número {numero}, {quantidade} {label}")



