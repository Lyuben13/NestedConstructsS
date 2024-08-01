import random


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__person_ID = random.randint(1, 100)

    def __get_id(self):
        return f'{self.__person_ID}\n'

    def get_info(self):
        return f"{self.__get_id()}Person first name - {self.first_name}; last name - {self.last_name}; age - {self.age}."

    def say_hi(self, text: str):
        person_info = self.get_info()
        return f"{text}! I am {self.first_name}"


person1 = Person('Joe', 'Black', 30)
print(person1.get_info())
person1.age = 35
print(person1.get_info())
print(person1.say_hi('Hi'))
print(person1.get_info())

# person1._Person__get_id = 121
# print(person1.get_info())
