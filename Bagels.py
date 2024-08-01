from random import random

NUM_DIGITS = 3
NUM_TRIES = 10


def give_clues(current_num: int, secret_num: int):
    if current_num == secret_num:
        print("You won!")
        return
    clues = []
    current_num = [x for x in str(current_num)]
    secret_num = [x for x in str(secret_num)]
    for i in current_num:
        if current_num.index(i) == secret_num.index(i):
            clues.append("Fermi")
        else:
            clues.append("Pico")
        # secret_num += str(current_num)
        # return secret_num
    return clues

def get_secret_num():
    secret_num = random.randit(1, 1000)

secret_num = 567
for i in range(10):
    current_guess = int(input("Enter number: "))
    current_guess = give_clues(current_guess, secret_num)
    print(current_guess)


# simple match case statement
# def runMatch():
#     current_num = eval(input("Enter a number: "))
#     secret_num = eval(input("Enter secret num: "))
#
#     # match case
#     match current_num == secret_num:
#         case 1:
#             print("Equal")
#         case 2:
#             print("Not equal")
#         case 3:
#             print("Error")
#         case _:
#             print("Not equal!")
#
#
# runMatch()


while True:
    pass



# def getSecretNum():
#    """Returns a string made up of NUM_DIGITS unique random digits."""
#    numbers = list('0123456789')  # Create a list of digits 0 to 9.
#    random.shuffle(numbers)  # Shuffle them into random order.
#
#     # Get the first NUM_DIGITS digits in the list for the secret number:
#
#      secretNum = ''
#
#      for i in range(NUM_DIGITS):
#          secretNum += str(numbers[i])
#       return secretNum
