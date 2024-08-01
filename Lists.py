# num_list = [int(num) for num in input().split()]
#
# print(num_list)

#
# num_list2 = []
#
# for i in range(1, 10):
#     num_list2.append(i)
#
#
#     print(i + 1)

#
# num_list = [num.__pow__(num) for num in range(1, 10)
#             if num % 2 == 0
#             ]
#
# print(num_list)
#
# num_list2 = []
#
# for i in range(1, 10):
#     if i % 2 == 0:
#         num_list2.append(i)
#
# print(num_list2)
#
# num_list3 = [x*y for x in range(1, 4) for y in range(1, 4)]
#
# print(num_list3)
#
# a = ["apple", "banana", "cherry"]
# b = ["Ford", "BMW", "Volvo"]
# a.append(b)
#
# print(b)
#
#
# num_list4 = [
#     [x*y for x in range(1, 4)]
#     for y in range(1, 4)
# ]
#
# print(num_list4)

#
# userLogs = ["admin","student","teacher","hr","user"]
# print(len(userLogs)) #5
# print(sorted(userLogs)) #['admin', 'hr', 'student', 'teacher', 'user']
# prices = [100, 250.45, 1200, 20.78]
# print(sum(prices)) #1571.23
# print(max(prices)) #1200
# print(min(prices)) #20.78
# print(sorted(prices)) #[20.78, 100, 250.45, 1200]

# userLogs = ['admin', 'student', 'teacher', 'hr', 'user', "hr"]
#
# # for i in userLogs:
# #     print(i)
# #
# # for i in range(len(userLogs)):
# #     # print(userLogs[i])
# #     print(f"{i + 1}: {userLogs[i]}")
#
# for key, value in enumerate(userLogs):
#     print(f"{key + 1}: {value}")

# userLogs.extend(['Horror', 'Sci-Fi'])
# print(userLogs)
# userLogs.append('manager')
#
# userLogs.append(["Mystery", "Romance"])
# print(userLogs)
#
# userLogs.insert(2, "manager")
# print(userLogs)
#
# userLogs.remove("hr")
# print(userLogs)
#
# userLogs.pop(9)
# print(userLogs)
#
# userLogs.remove("hr")
# print(userLogs)
#
# userLogs.index('Horror')
# # print(userLogs)
# #
# # removed_item = userLogs.pop(userLogs.index('manager'))
# # print(userLogs)
# # print(removed_item)
# # print(userLogs.count('manager'))
# # print(userLogs)
# # print(userLogs.count("manager"))
# # print(userLogs.index("manager"))
# # # userLogs.sort()
# # userLogs.reverse()
# # print(userLogs)
# # # print(sorted(userLogs, reverse=True))
# # userLogs.sort()
# # print(userLogs)
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list3 = [6, 7, 8]
# print(list2 is list1)  #True
# print(list3 is list1)  #False
#
# customers = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
# for i in range(len(customers)):
#     if customers[i] == 'Bob':
#         print(i)
#
# for i in range(len(userLogs)):
#     if userLogs[i] == "hr":
#         print(i)
#
# myTbl = [
#     [111, 112, 113],
#     [221, 222, 223]
# ]
#
# table2 = [[j for j in range(2)] for i in range(3)]
# print(table2)
#
# studScores = [['Bob', 11, 8, 10, 12], ['Jane', 12, 11, 11, 11], ['Kate', 7, 8, 9, 9]]
# for student in studScores:
#     print(student)
#
# for student in studScores:
#     print(student[0], max(student[1:]))

# Task1
user_name = input("Enter your name: ")

reversed_name = ''

for i in user_name[::-1]:
    reversed_name = reversed_name + i

print(reversed_name)

# Task2

user_name = input("Enter your string: ")

digits = 0
letters = 0

for i in user_name:
    if i.isdigit():
        digits +=1
    else:
        letters += 1
print(f"Result: Digits:{digits}, Letters:{letters}")

user_name1 = input("Enter string: ")
user_symbol = input("Enter symbol: ")

print(user_name1.count(user_symbol))

user_name2 = input("Enter string: ")
word = input("Enter word to replace: ")
replacement_word = input("enter replacement word: ")

print(user_name2.replace(word, replacement_word))










