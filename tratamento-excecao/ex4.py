def somar_elementos(lista, indice_1, indice_2):
    soma = 0

    try:
        soma = lista[indice_1] + lista[indice_2]
    except IndexError as e:
        print(f"Erro capturado pelo Python: {e}")
    except TypeError as e:
        print(f"Erro capturado pelo Python: {e}")
    
    return soma
    
lista = [5, 5]
response = somar_elementos(lista, 0, 4)
print(response)