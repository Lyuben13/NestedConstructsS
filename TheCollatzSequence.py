def collatz(number) -> int:
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


try:
    user_num = eval(input("Enter an Integer:\t"))

    result = user_num
    while user_num != 1:
        user_num = collatz(user_num)
except ValueError:
    print("Invalid Integer:\t")
