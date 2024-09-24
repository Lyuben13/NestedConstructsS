import random
from datetime import date


class Employee:
    hobby = 'Cooking'

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self._age = age
        self._employee_id = random.randint(1, 100)

    def _show_id(self):
        print(self._employee_id)

    def get_info(self):
        return (f'Employee first name - {self.firstName} '
                f'last name - {self.lastName} '
                f'age - {self._age}')

    def say_hi(self, greeting):
        print(f'{greeting}, I am {self.firstName}.')

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

    # Property for age with getter and setter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    # Property for employee_id (read-only)
    @property
    def employee_id(self):
        return self._employee_id

# Creating instances and using the class methods
employee1 = Employee('Peter', 'Б', 35)
print(employee1.get_info())
print(f'Hobby: {employee1.hobby}')
employee1.say_hi('Hi')
employee1.say_greeting()

# Setting and getting hobby using a class method
Employee.set_default_hobby('Football')
print(f'Updated Hobby: {employee1.hobby}')

# Creating an employee from birth year
employee3 = Employee.get_age_from_year('Jane', 'Doe', 1995)
print(employee3.get_info())

# Creating an employee from a string
employee4 = Employee.create_emp_from_str('Andy Jophnes 19')
print(employee4.get_info())
print(f'First Name: {employee4.firstName}')

# Using property to get and set age
print(f"Employee's age: {employee1.age}")
employee1.age = 36
print(f"Updated age: {employee1.age}")

# Accessing read-only employee_id
print(f"Employee ID: {employee1.employee_id}")
