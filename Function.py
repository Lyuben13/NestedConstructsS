# def hello():
#     print("Hello!")
#     print("World")
#
#
# hello()
#
#
# def calculate(a, b):
#     return a + b
#
#
# x = eval(input("Inp2ut x:"))
# z = eval(input("Input z:"))
# if calculate(x, z) <= 0:
#     y = x + z
# else:
#     y = x - z
# print("y = ", y)
#
#
# def checkCustomer(customer, customers):
#     result = 0
#     print("Client's positions in the list:")
#     for i in range(len(customers)):
#         if customers[i] == customer:
#             print(i)
#             result += 1
#     return result
#
#
# customerList = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
# myCustomer = 'Bob'
# if checkCustomer(myCustomer, customerList) > 1:
#     print("Customer", myCustomer, "will get a discount")


# def modify_Name(user_name) -> str:
#     new_name = user_name.upper()
#     return new_name
#     # print("Hello")
#
#
# # name = input("Input your name: ")
# # print(modify_Name(name))
#
# def check_customer(customer: str, customers: list) -> int:
#     result = 0
#     print("Client's position in the list:")
#
#     for i in range(len(customer)):
#         if customers[i] == customer:
#             print(i)
#             result += 1
#     return result
#
#
# customer_list = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
# customer_name = 'Bob'
#
#
# #
# # if check_customer(customer_name, customer_list) > 1:
# #     print(f"Customer {customer_name} will get a discount")
#
# def modify_name2(user_name: str):
#     new_name_upper = user_name.upper()
#     new_name_lower = user_name.lower()
#     return new_name_upper, new_name_lower
#
# #
# # name = input("Enter your name: ")
# # print(modify_name2(name))

# import random
#
# input("Enter some question:\t")
#
#
# def get_answer(answer_number):
#     if answer_number == 1:
#         return 'It is certain'
#     elif answer_number == 2:
#         return 'It is decidedly so'
#     elif answer_number == 3:
#         return 'Yes'
#     elif answer_number == 4:
#         return 'Reply hazy try again'
#     elif answer_number == 5:
#         return 'Ask again later'
#     elif answer_number == 6:
#         return 'Concentrate and ask again'
#     elif answer_number == 7:
#         return 'My reply is no'
#     elif answer_number == 8:
#         return 'Outlook not so good'
#     elif answer_number == 9:
#         return 'Very doubtful'
#
#
# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)
#
# def calculateExample1():
#     baseVar = int(input("input base variable: "))
#     resultVar = baseVar ** 2
#     print(f"The square of {baseVar} is: {resultVar}")
#
#
# calculateExample1()
# # print(baseVar)
#
# def print_function(name: str):
#     print(f"Hello, {name}")
#
#
#
# # name_printer = print_function

customers = ['AdminJane', 'adminBob', 'STUDENTbob', 'studentAlice', "Kate"]


def sayHello(customer) -> str:
    if customer.find("admin") != -1:
        print(f"Hello, admin - {customer}")
    elif customer.find("student") != - 1:
        print(f"Hello, student - {customer}")
    else:
        print(f"Hello, {customer}")


def greetings(customList: list[str], greetF: callable(str)):
    for c in customList:
        greetF(c.lower())


# greetings(customers, sayHello)

def factorialCalculation(n):
    if n == 0:
        return 1
    else:
        return n * factorialCalculation(n - 1)


# print(factorialCalculation(5))


def simpleDecorator(myFunction):
    print("Hello! I'm Decorator!")

    def simpleWrapper():
        print("Function starts working...")
        myFunction()
        print("See you!")

    return simpleWrapper


# def sayHi():
#     print("Welcome!")


# sayHiAdvanced = simpleDecorator(sayHi)
# sayHiAdvanced()
# @simpleDecorator
# def sayHi():
#     print("Welcome!")
#
#
# @simpleDecorator
# def send_text():
#     print("Some text...")
#
#
# sayHi()
# send_text()

def check_lucky_num(num: int) -> bool:
    num_string = str(num)
    first_half = sum([int(x) for x in num_string[:3]])
    second_half = sum([int(x) for x in num_string[3:]])

    if first_half == second_half:
        return True
    else:
        return False


#
# if check_lucky_num(int(input("Enter number here:\t"))):
#     print("\nLucky")
# else:
#     print("\nVery sad number")


def calculate_sum(num_list: list) -> None:
    print(sum(num_list))


repeating_random_nums = [12, 11, -17, 7, 11, 5, 5, -11, -17, -7, 18]
calculate_sum(repeating_random_nums)



