def has_minimum_characters(password, minimum):
    return len(password) >= minimum

def has_number(password):
    return any(char.isdigit() for char in password)

def has_upper_case(password):
    return any(char.isupper() for char in password)

def is_password_valid(password):
    minimun_characters = 8
    if(not has_minimum_characters(password, minimun_characters)):
        print(f"A senha deve ter no mínimo {minimun_characters} caracteres!")
        return False

    if(not has_number(password)):
        print("A senha deve conter um número!")
        return False

    if(not has_upper_case(password)):
        print("A senha deve conter uma letra maiúscula")
        return False

    return True
    

password = input("Informe a senha: ")

if(is_password_valid(password)):
    print("Senha cadastrada com sucesso")
