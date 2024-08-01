# myStr: str = "foobar"
# print(myStr[0])  #'f'
# print(myStr[1])  #'o'
# print(len(myStr) - 1)  #'r'


# str1 = "Hello,"
# str2 = " Admin"
# print(str1 + str2)
# str3 = str1 + str2
# print(str3)

# print(''.join([str1, str2]))

# print(str1 * 5)

# myStr: str = "python was created in the late 1980's by Guido van Rossum."
#
# print(myStr.capitalize()) # Python was created in the late 1980's by guido van rossum.
# print(myStr.lower()) #python was created in the late 1980's by guido van rossum.
# print(myStr.upper()) #PYTHON WAS CREATED IN THE LATE 1980'S BY GUIDO VAN ROSSUM.
# print(myStr.title()) #Python Was Created In The Late 1980'S By Guido Van Rossum.
# print(myStr.swapcase()) #PYTHON WAS CREATED IN THE LATE 1980'S BY gUIDO VAN rOSSUM.
#
# txt = "\t\nHello My Name Is PETER"
#
# x = txt.swapcase()
#
# print(x)

# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
#
# print(myStr.count('Python'))  #2
# print(myStr.count('Python', 20, 65))  #1
# print(myStr.count('Python', 10))  #1

# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
#
# print(myStr.startswith('P'))
# print(myStr.startswith('p'))
# print(myStr.startswith('w',7))
# print(myStr.endswith('!'))
# print(myStr.endswith('n',2,6))
#
#

# myStr = 'Python2021'
# print(myStr.isalnum())
# print(myStr.isalnum())
#
# myAge = "16"
# print(myAge.isdigit())
#
# myStr1 = "it was created in the late 1980's"
# print(myStr1.islower())
#
# myStr2 = "\t \n \t\t"
# print(myStr2.isspace())
#
# myName1 = "Guido van Rossum"
# print(myName1.istitle())
#
# myName2 = "GUIDO VAN ROSSUM"
# print(myName2.isupper())




# # Python Program to Print Mirrored Right Triangle Star Pattern
#
# rows: int = int(input("Please Enter the Total Number of Rows  : "))
#
# print("Mirrored Right Triangle Star Pattern")
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print('*', end = '  ')
#     print()


myStr = "*"

print(myStr.center(10))
print(myStr.center(10,'*'))
print(myStr.center(10))



myStr = "Phyton\n\t\tPython- cool!"
print(myStr.expandtabs())

myStr = "Python- cool!"
print(myStr.ljust(20))
print(myStr.ljust(20,'@'))
print(myStr.ljust(5))


myStr = "          Python- cool!     "
print(myStr.lstrip())
print(myStr.rstrip())
print(myStr.strip())

myStr = "@;        Python- cool!     @"
print(myStr.lstrip('@;'))
print(myStr.rstrip('@'))
print(myStr.strip('@'))

myStr = "123"
print(myStr.zfill(5))

myStr = "+123"
print(myStr.zfill(5))

myStr = "1234567890"
print("")
print(myStr[2:8:2]) #357
print(myStr[8:2:-2]) #975
print(myStr[::-1]) #0987654321
print(myStr[5::2]) #680
print(myStr[-1::-2]) #08642
print(myStr[:len(myStr):3]) #1470

print('\'Python Programming: An Introduction to Computer Science\'')
print("\"Python Programming: An Introduction to Computer Science\"")
print("15\\2")


myStr = "\x2C"
print(myStr) # ,

myStr = "\053"
print(myStr) # +

myStr = "In Python strings, the backslash '\\' is a special character. It is used in representing certain whitespace characters: '\\t' is a tab, '\\n' is a newline"
print(myStr)

normalStr = "This is a \nnormal string"
print(normalStr)
rawStr = r"This is a \n raw string"
print(rawStr)


strMsg = "Your salary is {0:3.0f}".format(200.846)
print(strMsg) # Your salary is 200.85

print("Enter your salary:")
my_Str: float = float(input())
print(f"\nYour salary is {my_Str:0.0f}")













