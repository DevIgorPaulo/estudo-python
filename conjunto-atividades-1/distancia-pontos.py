import math

def diferencaPontos(p1, p2):
    return (p2 - p1) ** 2

x1 = float(input('Informe o x1: '))
y1 = float(input('Informe o y1: '))
x2 = float(input('Informe o x2: '))
y2 = float(input('Informe o y2: '))

distanciaX = diferencaPontos(x2, x1)
distanciaY = diferencaPontos(y2, y1)

distancia = math.sqrt(distanciaX + distanciaY)

print(f"A distância entre os pontos é: {distancia:.2f}")
