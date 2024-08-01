# # userTypes = ["admin","student","teacher"],
# userTypes1 = ()
# # userTypes[0]= "user"
# userTypes2 = tuple()
import sys
from typing import List


# print(userTypes)

# def askPersonalInfo():
#     while True:
#         firstName = input("Input your first name: \t")
#         lastName = input("Input your last name: \t")
#         yearsBirth = input("Input your year of birth: \t")
#         gender = input("Input your gender (M, F): \t")
#         if (firstName == ""
#                 or lastName == ""
#                 or yearsBirth == ""
#                 or gender == ""
#                 not in ("F", "M")
#             or not yearsBirth.isdigit()
#         ):
#             print("Wrong data!")
#         else:
#             return firstName, lastName, yearsBirth, gender
#
#
# for_print = askPersonalInfo()
# print(for_print)

def askHobby():
    hobbyInd = 1
    hobbyList: list[str] = []
    while True:
        firstName = input("Input your first name: \t")
        lastName = input("Input your last name: \t")
        hobbyName = input(f"Name of the hobby {hobbyInd}:")
        yearsBirth = input("Input your year of birth: \t")
        gender = input("Input your gender (M, F): \t")

        if (hobbyName == ""
                or firstName != ""
                or lastName != ""
                or yearsBirth != ""
                or gender == "" in ("F", "M")
                or yearsBirth.isdigit()):
            hobbyList.append(hobbyName)
        elif hobbyName or "end".lower().split().append("end"):
            print("Wrong data!")
            exit(hobbyName == 'end')

        else:

            return firstName, lastName, yearsBirth, hobbyName, gender


forAskHobby = askHobby()
print(forAskHobby)
