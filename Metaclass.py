from typing import Protocol, runtime_checkable


# print(type("Peter"))
#
#
# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         print(f'Creating instance of {cls}')
#         instance = super().__new__()
#         return instance
#
#     def __init__(self, value):
#         self.value = value
class Vehicle:
    def move(self):
        return 'The vehicle is moving'


class AttributeNamingMeta(type):
    def __new__(cls, name, bases, dct: dict):
        if Vehicle not in bases:
            bases = (Vehicle,) + bases
        for attr_name in dct:
            if not attr_name.startswith('_') and not callable(dct[attr_name]):
                raise AttributeError(f'Attribute "{attr_name}" in class "{name}" does not start with underscore.')

        dct['from_AttributeMeta'] = 'AttributeNamingMeta'

        if 'required_attr' in dct:
            raise TypeError(f"Class '{name}' must define 'required_method'")

        return super().__new__(cls, name, bases, dct)


class Car(metaclass=AttributeNamingMeta):
    _engine = 6.2
    _doors = 4

    def required_method(self):
        pass


#
# car1 = Car
# print(car1.from_AttributeMeta)
# print(car1.move())
@runtime_checkable
class Item(Protocol):
    price: float
    discount: int


class Book:
    def __init__(self, title, author, price, discount):
        self.title = title
        self.author = author
        self.price = price
        self.discount = discount


class Product:
    def __init__(self, name, price, disc, producer):
        self.name = name
        self.price = price
        self.disc = disc
        self.producer = producer


def calculate_total_price(objs):
    total = 0

    for obj in objs:
        if isinstance(obj, Item):
            total += obj.price * (1 - obj.discount / 100)

    else:
        print(f"Incompatible type: {obj.__class__.__name__}")

    return total


books_and_products = [
    Book("Python", "John Smith", 100, 20),
    Product("Tea", 50, 10, "Some Brand")
]

total_price = calculate_total_price(books_and_products)
print(total_price)


class Drawable(Protocol):
    def draw(self) -> None:
        pass


class Circle:
    def draw(self) -> None:
        print("Drawing a circle")


class Square:
    def draw(self) -> None:
        print("Drawing a squere")


def render(shape: Drawable):
    shape.draw()


render(Circle())
render(Square())
