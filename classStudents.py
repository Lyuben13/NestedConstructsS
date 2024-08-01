class Student:
    spec = 'Computer science'

    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def show_info(self):
        return f"Student {self.name} is {self.age} years old."

    def show_message(self, message_text):
        return f"Student {self.name} says '{message_text}'."


student1 = Student(1,'Gosho', 20)
student2 = Student(2,'Checho', 27)
print("Student's 1 info:")
print(student1.show_info())
print(student1.show_message('Hello'))
print(student1.spec)
print("\n\rStudent's 2 info:")
print(student2.spec)
print(student2.show_info())
print(student2.show_message('Hi'))


