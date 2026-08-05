def is_student_approved(total_lessons, absences, grade):
    absence_percentage  = absences / total_lessons * 100

    if(absence_percentage  > 25):
        return 0

    if(grade < 6):
        return 0

    return 1

is_approved = is_student_approved(50, 5, 6)
print(is_approved)