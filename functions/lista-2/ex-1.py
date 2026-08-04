def classifica_idade(idade):
    if idade < 0:
        return 'Idade Inválida' 
    if idade < 12:
        return 'Criança'
    if idade < 18:
        return 'Adolecente'
    if idade < 60:
        return 'Adulto'

    return 'Idoso'

idade = 12
print(classifica_idade(idade))
