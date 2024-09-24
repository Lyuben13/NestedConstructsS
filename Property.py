class Product:
    def __init__(self, name, price):
        self._name = name
        self.price = price
        self.discount = 0.25

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Name must be a string')

    @name.deleter
    def name(self):
        self._name = None


prod1 = Product('Apple', 1.25)

prod1.name = 600
print(prod1.name)

prod1.name = 'Red Apple'
print(prod1.name)

del prod1.name
print(prod1.name)
