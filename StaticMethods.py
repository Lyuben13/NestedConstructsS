import random
from datetime import date


class Employee:
    hobby = 'Coocking'

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
    def set_defaut_hobby(cls, hobby):
        cls.hobby = hobby

    @classmethod
    def get_age_from_year(cls, firstName, lastName, yearBirth):
        employeeAge = date.today().year - yearBirth
        return cls(firstName, lastName, employeeAge)

    @classmethod
    def create_emp_from_str(cls, emp_data: str):
        firstName, lastName, age = emp_data.split()


employee1 = Employee('Peter', 'Buzukov', 35)
print(employee1.get_info('Hi'))
print(employee1.hobby)
print(employee1.say_greeting())

Employee.set_defaut_hobby('Football')
employee2 = Employee('Peter', 'Buzukov', 35)
print(employee2.hobby)
print(employee2.get_info('Hi'))
employee3 = Employee.get_age_from_year('Jane', 'Doe', 1995)
print(employee3.get_info(employee3))

employee4 = Employee.create_emp_from_str('Andy Jophnes 19')
print(employee4.get_info())
print(employee4.firstName)
# class Developer:
#     def get_info(self):
#         print('I am a developer')
#
# dev1 = Developer()
#
# def get_info(obj):
#     return obj.get_info()
#
# get_info(employee1)
# get_info(dev1)
