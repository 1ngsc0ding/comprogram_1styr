# ให้นศ.เขียน Class สําหรับเก็บข้อมูลนักเรียน (Student) ได้แก่ student_id, name, course, age โดยมีmethod
# show() เพื่อแสดงข้อมูลของนักเรียนคนนั้นๆ (Object)
# จากนั้นให้เขียนโปรแกรมอ่านข้อมูลของนักเรียนจาก text file และสร้าง array ของ Student (object)
# พร้อมเขียนฟังก์ชันที่จะรับ array ของ Student แล้วแสดงข้อมูลของนักเรียน ที่มีอายุ (age) น้อยที่สุด
# โดยเรียกใช้method show()

class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = int(age)

    def show(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Age:", self.age)

def read_student():
    students = []
    with open("student.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            student = Student(data[0], data[1], data[2], data[3])
            students.append(student)
    return students

def show_youngest(students):
    youngest = students[0]
    for student in students:
        if student.age < youngest.age:
            youngest = student
    print("Youngest Student")
    youngest.show()

students = read_student()

show_youngest(students)