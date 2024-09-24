import random
from datetime import date


# Декоратор за промяна на цената
def changePriceDecorator_v1(myFunction):
    print("Hello! Let's change your prices...")

    def simpleWrapper(argList):
        print("I've got a list of prices with {} elements. Function starts working...".format(len(argList)))
        result = myFunction(argList)
        resultWithDisc = list(map(lambda x: x * (1 - 0.15), result))
        print("Let's set a discount..")
        return resultWithDisc

    return simpleWrapper


# Декоратор за метод в клас
def methodDecorator(method_to_decorate):
    def wrapper(self):
        print("General information:")
        method_to_decorate(self)

    return wrapper


# Декоратор с памет за извиквания
class myDecorator:
    def __init__(self, fn):
        self.fn = fn
        self.__memoryCall = []

    def __call__(self, num1, num2):
        result = self.fn(num1, num2) ** 2
        self.__memoryCall.append(result)
        return result

    def showMemoryState(self):
        print(f"Current memory state: {self.__memoryCall}")


# Клас Employee
class Employee:
    hobby = 'Cooking'

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self._age = age
        self._employee_id = random.randint(1, 100)

    def _show_id(self):
        print(self._employee_id)

    def get_info(self, personal_id):
        return (f'Employee first name - {self.firstName}'
                f' last name - {self.lastName}',
                f'age - {self._age}')

    def say_hi(self, greeting):
        print(self.get_info(greeting))
        print(f'{greeting} I am {self.firstName}.')

    @staticmethod
    def say_greeting():
        print('Nice to meet you!')

    @classmethod
    def set_default_hobby(cls, hobby):
        cls.hobby = hobby

    @classmethod
    def get_age_from_year(cls, firstName, lastName, yearBirth):
        employeeAge = date.today().year - yearBirth
        return cls(firstName, lastName, employeeAge)

    @classmethod
    def create_emp_from_str(cls, emp_data: str):
        firstName, lastName, age = emp_data.split()
        return cls(firstName, lastName, int(age))


# Клас Book с декориран метод
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @methodDecorator
    def showInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


# Декорирана функция за промяна на цени
@changePriceDecorator_v1
def toPriceNew(priceList):
    return list(map(lambda x: x * 27.5, priceList))


# Пример за декоратор с памет за извиквания
@myDecorator
def addNums(x, y):
    return x + y


# Тестове и извиквания
pricesUSD = [100.34, 35, 67.99, 25.5]
print(toPriceNew(pricesUSD))

book1 = Book("Python Crash Course", "Eric Matthes", 624)
book1.showInfo()

employee1 = Employee('Peter', 'Б', 35)
print(employee1.get_info('Hi'))
print(employee1.hobby)
print(employee1.say_greeting())

Employee.set_default_hobby('Football')
employee2 = Employee('Peter', 'Б', 35)
print(employee2.hobby)
print(employee2.get_info('Hi'))
employee3 = Employee.get_age_from_year('Jane', 'Doe', 1995)
print(employee3.get_info(employee3))

employee4 = Employee.create_emp_from_str('Andy Jones 19')
print(employee4.get_info('Hello'))
print(employee4.firstName)

print(addNums(2, 3))
addNums.showMemoryState()

print(addNums(3, 3))
addNums.showMemoryState()

print(addNums(4, 3))
addNums.showMemoryState()
