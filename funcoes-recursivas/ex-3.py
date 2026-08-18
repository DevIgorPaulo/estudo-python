def print_number(number):
    if number < 10:
        print(number)
        return

    print(number % 10)
    print_number(number // 10)

print_number(3214)