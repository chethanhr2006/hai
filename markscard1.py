class Student:
    def __init__ (self, roll_no, name):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def calculate_average(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        average = total / len(self.__marks)
        return average

    def is_passed(self):
        has_passed = all(mark >= 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has not passed")

    def calculate_grade(self):
        print("Grade: ", end=" ")
        average = self.calculate_average()
        if average >= 90:
            print("A")
        elif average >= 85:
            print("B")
        else:
            print("C")

class ReportCard:
    @staticmethod
    def generate(student: Student):
        student_marks = student.get_marks()
        print(f"Name: {student.name} \t Roll No.: {student.roll_no}")
        print("----Marks----")
        for subject, marks in student_marks.items():
            print(f"{subject} - {marks}")
        print("--------")
        print(f"Average: {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()
        print("\n")

class ClassRoom:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def calculate_class_average(self):
        if not self.__students:
            return 0
        total = 0
        for student in self.__students:
            total += student.calculate_average()
        return total / len(self.__students)

    def get_students_list(self):
        for i, student in enumerate(self.__students):
            print(f"{i+1}. {student.name}")

a = Student(1, "John")
a.add_marks("math", 96)
a.add_marks("science", 95)

c = ClassRoom("10", "A")
c.add_student(a)

b = Student(2, "Alice")
b.add_marks("math", 86)
b.add_marks("science", 88)
c.add_student(b)

print("Students in class:")
c.get_students_list()
print(f"Class average: {c.calculate_class_average()}")