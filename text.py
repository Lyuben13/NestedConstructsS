# class ClassWithRegularAttributes:
#     def __init__(self, someParameter):
#         self._someAttribute = someParameter
#
#     @property
#     def someAttribute(self):
#         return self._someAttribute
#     @someAttribute.setter
#     def someAttribute(self, value):
#         self._someAttribute = value
#
#     @someAttribute.deleter
#     def someAttribute(self):
#         del self._someAttribute
#
# obj = ClassWithRegularAttributes('some initial value')
# print(obj.someAttribute)  # Prints 'some initial value'
# obj.someAttribute = 'changed value'
# print(obj.someAttribute)  # Prints 'changed value'
# del obj.someAttribute  # Deletes the someAttribute attribute.


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
rect = Rectangle(a, b)

print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

