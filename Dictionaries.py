# # book_dict = {'author': 'Eric Matthes',
# #              'title': 'Python Crash Course',
# #              'price': 14.43,
# #              'reading age': '12 years and up',
# #              'language': 'English'
# #              }
# #
# # book_dict["pages"] = 350
# # print()
# #
# # # info_type = input("What would you like to add?\t")
# # #
# # # if info_type in book_dict:
# # #     print(book_dict[info_type])
# # # else:
# # #     print("Sorry.")
# # #
# # # new_info = input("What would you like to add?\t")
# # # if new_info != "":
# # #     new_info_value = input(f"Input value for: {info_type}\t")
# # #     if new_info_value == "":
# # #         print(f"No value for the key {new_info_value}\t")
# # #
# # #     else:
# # #         book_dict[new_info] = new_info_value
# # # else:
# # #     print("No key!")
# # #
# # # book_dict.update([("pages", 600), ("discount", True)])
# #
# # for k, v in book_dict.items():
# #     print(f"{k}: {v}")
# #
# # print(list(book_dict.keys()))
# #
# #
#
# #
users = [
    {'name': 'Hanna', 'age': 10, 'login': 'user56'},
    {'name': 'Mark', 'age': 15, 'login': 'usER111'},
    {'name': 'Jane', 'age': 17, 'login': 'superGirl'},
    {'name': 'Jack', 'age': 7, 'login': 'userJack'}
]

users12 = list(filter(lambda user: user['age'] > 12, users))
for user in users12:
    for key, val in user.items():
        print(f"{key}:{val}")


# sorted_by_name = sorted(users, key=lambda x: x['login'])
# for users in sorted_by_name:
#     for k, v in users.items():
#         print(f"{k}: {v}")

# # key_name = input("Input info type:\t")
# # key_value = input("Input info value:\t")
# # # key_value = key_value if key_name != 'age' else int(key_value)
# # if key_name == 'age':
# #     key_value = int(key_value)
# #
# # isElementFound = False
# # for user in users:
# #     if user.get(key_name) == key_value:
# #         print("Element is found!")
# #         for key, val in user.items():
# #             print(f"{key}:{val}")
# #         isElementFound = True
# #         break
# # if not isElementFound:
# #     print("Element is not found!")
#
#
# film_dict = {'originalTitle': 'Forever',
#              'creator': 'Matthew Miller',
#              'rate': 8.3,
#              'description': 'A 200-year-old man worksin the New York City Morgue trying to find a key to unlock the curse of his immortality.',
#              'years': [2014, 2015]
#              }
#
# # for key, value in film_dict.items():
# #     print("{}:{}".format(key, value))
#
# sorted_tuples = sorted((film_dict.items()), key=lambda x: x[0])
# print(sorted_tuples)
#
# # for item in sorted_tuples:
# #     print(item)
#
# key_list = list(sorted(film_dict.keys()))
# # print(key_list)
# # sortedKeys = sorted(keyList)
# # print(sortedKeys)
# for key in key_list:
#     print(f"{key}:{film_dict[key]}")
#

