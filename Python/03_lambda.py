students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016305),
        ('김지영', 4.3, 2016302),
]

a = sorted(students, key=lambda student: (student[1], student[2]))
b = sorted(students, key=lambda student: (student[1]))
c = sorted(students, key=lambda student: (student[2], student[1]))
d = sorted(students, key=lambda student: (student[2]))

print(a)
print(b)
print(c)
print(d)
print()

students.sort(key=lambda x:(x[1], x[2]))
print(students)
