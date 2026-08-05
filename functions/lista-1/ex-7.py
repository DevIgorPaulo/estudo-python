def get_factorial(number):
    if number < 0:
        return "Não existe fatorial de número negativo"

    factorial = 1
    counter = 2

    while counter <= number:
        factorial *= counter
        counter += 1

    return factorial

number = 7
print(f"O fatorial de {number} é {get_factorial(number)}")