class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(f"Person first name - {self.first_name}; last name - {self.last_name}; age - {self.age}")

    def getHi(self, msgText):
        print(f"{msgText}! I am {self.first_name}")


person1 = Employee("Joe", "Black", 30)
person2 = Employee("Kate", "Bekinsel", 34)
person1.get_info()
person1.getHi("Hi")
person2.get_info()
person2.getHi("Hello")


class Student(Employee):
    spec = "Computer Science"

    def __init__(self, first_name, last_name, age, mean_score):
        super().__init__(first_name, last_name, age)
        self.mean_score = mean_score

    def get_info(self):
        super().get_info()
        print(f"Score - {self.mean_score}")

    def is_successful(self):
        return self.mean_score >= 75


class Developer(Employee):
    def __init__(self, first_name, last_name, age, job_title, salary, seniority):
        super().__init__(first_name, last_name, age)
        self.job_title = job_title
        self.salary = salary
        self.seniority = seniority

    def get_info(self):
        super().get_info()
        print(f"Job title - {self.job_title}; Salary - {self.salary}; Seniority - {self.seniority} years")

    def get_sick_leave(self):
        if self.seniority > 5:
            return 3
        return 1


# Testing the Student class
student1 = Student('Joe', 'Black', 30, 78)
print(f'{student1.first_name} successful? - {student1.is_successful()}')
print(student1.spec)
student1.get_info()

# Example usage of the Developer class
developer1 = Developer('Alice', 'Smith', 28, 'Software Developer', 85000, 6)
developer1.get_info()
print(f'{developer1.first_name} gets {developer1.get_sick_leave()} sick leave days.')

