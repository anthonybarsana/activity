class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}.")

student1 = Student("Anthony", 19, "Information Technology")
student2 = Student("Bob", 22, "Mechanical Engineering")
student3 = Student("Charlie", 19, "Mathematics")


student1.introduce()
student2.introduce()
student3.introduce()