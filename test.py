# import random
#
# random_nums = [
#     [random.randint(-20, 20) for x in range(3)]
#     for y in range(3)
# ]
#
# flat_nums_list = []
#
# for flat_nums_list in random_nums:
#     print(' '.join(str(n) for n in flat_nums_list))
#
# for inner_list in random_nums:
#     for num in inner_list:
#         flat_nums_list.append(num)
#
# print(random_nums)
# print(flat_nums_list)

repeating_random_nums = [12, 11, -17, 7, 11, 5, 5, -11, 17, -7, 18]

# non_repeating_list = []
# for non_repeating_list in repeating_random_nums:
#     if isinstance(repeating_random_nums, list):
#         for nested_temp in repeating_random_nums:
#             print(nested_temp)

digit = 0
found = []
found_again = []

for digit in repeating_random_nums:
    if digit in found_again:
        continue
    if digit in found:
        found.remove(digit)
        found_again.append(digit)
    else:
        found.append(digit)

print(found)
