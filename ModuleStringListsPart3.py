import random

random_nums = []
for x in range(10):
    random_nums.append(random.randint(-20, 20))

# first_positive = 0
# last_positive = 0
#
# for i in random_nums:
#     if i > 0:
#         first_positive = i
#         break
#
# for i in random_nums[::-1]:
#     if i > 0:
#         last_positive = i
#         break
#
# print(random_nums)
# print(random_nums.index(first_positive))
# print(random_nums.index(last_positive))
#
# print("\r\n")
# first_index = random_nums.index(first_positive)
# last_index = random_nums.index(last_positive)
# first_last = random_nums[first_index: last_index]
# print(sum(first_last))
#
# print("\r\n")
# positive_indices = [i for i, x in enumerate(random_nums)
#                     if x > 0
#                     ]
# if positive_indices:
#     first_pos_index = positive_indices[0]
#     last_pos_index = positive_indices[-1]
#     sum_between_positives = sum(random_nums[first_pos_index + 1:last_pos_index])
# else:
#     sum_between_positives = 0
#
# print(f"Sum between the smallest and the largest element: {sum_between_positives}")
#
# print("\n\r")

even_nums = [num for num in random_nums if num % 2 == 0]

even_nums_loop = []
for i in random_nums:
    if i % 2 == 0:
        even_nums_loop.append(i)

odd_nums = [num for num in random_nums if num % 2 != 0]

negative_nums = [num for num in random_nums if num < 0]

positive_nums = [num for num in random_nums if num > 0]


print(random_nums)
print(even_nums)
print(odd_nums)
print(negative_nums)
print(positive_nums)


