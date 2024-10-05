students = ['Howard', 'callem', 'christian']
for i in range(len(students)):
    students[i] = students[i].upper()

def find_student(student):
    for s in students:
        if s == student.upper():
            return True
    return False

def remove_student(student):
    for s in students:
        if s == student.upper():
            students.remove(s)


def add_student(student):
    students.append(student.upper())

new_students = {}
new_students['name'] = 10
print(new_students)

add_student("john cena")

for s in students:
    print(s)