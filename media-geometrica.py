import math 

n1 = float(input("Informe o 1° número: "))
n2 = float(input("Informe o 2° número: "))

n2Cubo = n2 ** 3
mediaGeometrica = math.sqrt(n1 * n2)

print(f"O cubo de {n2} é {n2Cubo}")
print(f"A média geométrica entre {n1} e {n2} é {mediaGeometrica:.2f}")
