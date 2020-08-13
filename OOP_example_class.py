class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

while True:
    name = str(input('Name: '))
    age = int(input('Age: '))
    grade = float(input('Grade: '))
    option = ' '
    while option not in 'YN':
        option = str(input('New student? [Y/N]')).strip().upper()
    if option == 'N':
        break
print(Student)
