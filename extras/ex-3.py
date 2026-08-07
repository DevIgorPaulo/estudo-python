def calculate_withdrawal(value):
    if value % 10 != 0:
        print("Valor Inválido!")
        return

    available_bills = [100, 50, 20, 10]

    bills = {}
    rest = value

    for available_bill in available_bills:
        bills[available_bill] = rest // available_bill
        rest = rest % available_bill

    show_bills(bills)

def show_bills(bills):
    for bill, quantity in bills.items():
        if quantity > 0:
            print(f"{bill}: {quantity}")


withdrawal = int(input("Informe o valor que deseja sacar (deve ser múltiplo de 10): "))
calculate_withdrawal(withdrawal)
