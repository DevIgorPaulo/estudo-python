def get_elactorate(age):
    if age < 16:
        return 'Não Eleitor'
    if 18 <= age <= 65:
        return 'Eleitor obrigatório'

    return 'Eleitor Facultativo'

age_1 = 12  
age_2 = 19  
age_3 = 68

print(f"O eleitor de {age_1} anos é: {get_elactorate(age_1)}")
print(f"O eleitor de {age_2} anos é: {get_elactorate(age_2)}")
print(f"O eleitor de {age_3} anos é: {get_elactorate(age_3)}")