def get_conceito_nota(nota):
    if 9 <= nota <= 10:
        return 'A'
    elif 8 <= nota < 9:
        return 'B'
    elif 7 <= nota < 8:
        return 'C'
    elif 6 <= nota < 7:
        return 'D'
    elif nota < 6:
        return 'F'
    else:
        return "Nota invalida"

conceito = get_conceito_nota(1)

print("Conceito da Nota: ", conceito)