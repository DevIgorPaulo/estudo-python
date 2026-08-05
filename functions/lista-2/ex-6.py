def student_situation(grade_1, grade_2, grade_3):
    mean_grade = (grade_1 + grade_2 + grade_3) / 3

    if mean_grade < 0 or mean_grade > 10:
        return 'Média inválida!'
    if mean_grade >= 7:
        return 'Aprovado'
    if mean_grade >= 5:
        return 'Recuperação'

    return 'Reprovado'

grade_1 = 2
grade_2 = 7
grade_3 = 2
print(student_situation(grade_1, grade_2, grade_3))