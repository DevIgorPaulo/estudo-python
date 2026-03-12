distancia = float(input("Digite a distância em Km: "))
velocidadeMedia = float(input("Digita a velocidade média em Km/H: "))

tempo = distancia / velocidadeMedia                                                                                                                                                                                                                                                                                                                                               
tempoSegundos = int(tempo * 3600)

horas = tempoSegundos // 3600
segundosRestantes = tempoSegundos % 3600

minutos = segundosRestantes // 60
segundos = int(segundosRestantes % 60)

print(f"O tempo media é de {tempo:.2f} horas")
print(f"{horas}:{minutos}:{segundos}")