class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def show(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Weight:", self.weight, "kg")
        print("Height:", self.height, "m")

    def getBMI(self):
        if self.height <= 0:
            return 0
        return self.weight / (self.height ** 2)


class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        super().show()
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("GPA:", self.gpa)
        print("BMI:", round(self.getBMI(), 2))

class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        super().show()
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("BMI:", round(self.getBMI(), 2))

student1 = Student("Ing", "Bangkok", 50, 1.60, "66001", "Computer Engineering", 3.50)
employee1 = Employee("Mild", "Nonthaburi", 55, 1.65, "E001", "IT", 25000)

print("Student Information")
student1.show()

print("\nEmployee Information")
employee1.show()