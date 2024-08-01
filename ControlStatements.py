# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")
import time

# import time
#
# number = 0
#
# while number !=15:
#     number +=1
#     print(f"\n{number} Is still not 15")
#     time.sleep(0.6)


# floor = 1
# energy = 70
# print("I'm on the", floor, "floor")
# while floor != 5:
#     step = 0
#     if floor == 3:
#         print("I will take an elevator")
#         break
#     while step != 20:
#         step += 1
#         energy -= 1
#         if energy == 0:
#             print("I'm tired, I will rest a little")
#             time.sleep(5)
#             energy += 70
#     floor += 1
#     print("Now I'm on the", floor, "floor")
# print("I've got to the right floor")

# x = 1
# while x <= 10:
#     print(x)
#     x += 1
#     break
#


# number = 5
# while True:
#     print(number)
#     number += 1
#     if not (number < 5):
#         break


# number = 0
# count = 0
#
# while count < 5:
#     number += 1
#     if number % 2 == 1:
#         continue
#
#     print(number)
#     count += 1


# number = 0
# while number < 300:
#     number += 1
#     if number % 3 == 0 and number % 5 != 0:
#         print(number, "divedes by 3")
#     elif number % 3 == 0:
#         if number % 5 == 0 and number % 7 != 0:
#             print(number, "divides by 3 and 5")
#         elif number % 5 == 0 and number % 7 == 0:
#             print(number, "divides by 3 and 5 and 7")

#
# number = 0
# while number < 300:
#     number += 1
#     if number % 3 != 0:
#         continue
#     elif number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 7 != 0:
#         print(number, "divides by 3 and 5")
#     else:
#         print(number, "divides by 3 and 5 and 7")


# number = 1
# while number <= 5:
#     if number == 4:
#         break
#
#     print(number)
#     number += 1
# else:
#     print("I've counted from 1 to 5!")
#
# try:
#   print(x)
# except:
#   print("An exception occurred")


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1
#
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = "hello"
#
# if type(x) is int:
#     pass
# else:
#     raise TypeError("Only integers are allowed")

