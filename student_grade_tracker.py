class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print("The grade is added.")
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")

    def calculate_avg(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Roll no: {self.roll_no}")
        print(f"Grades: {self.grades}")
        avg = self.calculate_avg()
        print(f"Average grade: {avg:.2f}")


student = Student("Aravind", 12)
student.add_grade(8)
student.add_grade(9)
student.add_grade(9)
student.add_grade(8)
student.display_details()
