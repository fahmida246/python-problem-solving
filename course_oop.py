class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_result(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)

    def avg_grade(self):
        num = 0
        for stu in self.students:
            num += stu.get_result()
        return num / len(self.students)


stu = Student("mahi", 12, 95)
stu1 = Student("nidhi", 13, 75)
print(stu)
print(stu.get_result())
cour = Course("python", 2)
cour.add_student(stu)
cour.add_student(stu1)
print(cour.avg_grade())
print(cour.students)
print(cour.students[0].name)
