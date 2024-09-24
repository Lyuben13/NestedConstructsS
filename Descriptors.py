class MyDescriptor1:
    def __init__(self, name=""):
        print("Descriptor's __init__ was started...")
        self.name = name

    def __get__(self, obj, objtype):
        print(f"Descriptor's __get__(instance={obj}, objtype={objtype}) was started...")
        return "{} was processed".format(self.name)

    def __set__(self, obj, name):
        print(f"Descriptor's __set__(instance = {obj}, name = {name}) was started...")
        if isinstance(name, str):
            self.name = name
        else:
            print("Name should be string")


class User:
    userName = MyDescriptor1()


user1 = User()
user1.userName = "Jack"
print(user1.userName)

user1 = User()
user1.userName = "Jack"
print(user1.userName)
user1.userName = 111
print(user1.userName)
