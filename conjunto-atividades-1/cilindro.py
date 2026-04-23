
import math

altura = float(input("Informe a altura(M): "))
raio = float(input("Informe o raio(M): "))

areaBase = 3.14 * raio ** 2
areaLateral = 2 * 3.14 * raio * altura
areaTotal = areaBase * 2 + areaLateral

litrosNecessarios = areaTotal / 3
latasNecessarias = math.ceil(litrosNecessarios / 5)

precoLatas = latasNecessarias * 20
print(f"Serão necessárias {latasNecessarias} latas de tinta custando R$ {precoLatas:.2f}".replace('.', ','))

