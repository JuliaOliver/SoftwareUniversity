import math

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

student_max_bonus = 0
student_max_bonus_attendaces = 0

for i in range(students_count):
    student_attendances = int(input())

    student_total_bonus = student_attendances / lectures_count * (5 + additional_bonus)

    if student_total_bonus > student_max_bonus:
        student_max_bonus = student_total_bonus
        student_max_bonus_attendaces = student_attendances

print(f"Max Bonus: {math.ceil(student_max_bonus)}.")
print(f"The student has attended {student_max_bonus_attendaces} lectures.")
