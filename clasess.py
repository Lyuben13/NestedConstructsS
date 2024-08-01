class Animal:
    def __init__(self, name, legs, tail):
        self.name = name
        self.legs = legs
        self.tail = tail

    def make_sounds(self):
        print('The animal says "brrr".')


class Dog(Animal):
    def make_sounds(self):
        print('The animal says "woof".')


class Cat(Animal):
    def make_sounds(self):
        print('The animal says "meow".')


# cat1 = Cat('Rino', 4, 'furry')
# cat1.make_sounds()

animal1 = Animal('Unknown', 8, 'no')
Animal.make_sounds(animal1)







