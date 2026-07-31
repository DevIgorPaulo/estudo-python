def maiorValor(v1, v2, v3):
    if v1 > v2:
        if v1 > v3:
            return v1
        else:
            return v3
    elif v2 > v3:   
        return v2
    else: 
        return v3

maior = maiorValor(9, 2, 6)
print(maior)

        