# try:
#     amount = int(input("Enter the amount of received items: "))
#     items_type = input("Specify the type of received items: ")
#     parts_number = int(input("Enter the number of parts: "))
#     parts_amount = amount / parts_number
#     print("Supply of", amount, items_type, "saved")
#     print("Each of", parts_number, "parts consists of", parts_amount, items_type)
# except ValueError:
#     print("Amount should be an integer")
# except ZeroDivisionError:
#     print("You cannot divide the delivery into 0 parts")
# finally:
#     print("The program has finished")

# try:
#     apples = int(input("Enter the amount of apples you have: "))
#     if apples < 0:
#         raise Exception
#     print("You have", apples, "apples")
# except Exception:
#     print("You can't have -10 apples")
#
# try:
#     x = 1/0
# except Exception as ex:
#     print(ex)

def devision_func(num1: int, num2: int):
    return num1 / num2


num1 = int(input())
num2 = int(input())
try:
    print(int(num1/num2))
except ZeroDivisionError:
    print("Cannot divide by 0!")
result = devision_func(10,2)
print(result)

try:
    result = int(input("Enter a number: "))
    print(result)
except ValueError:
    print("Wrong input")

