# # Subject
# class Subject:
#     def __init__(self):
#         self.observers = []  # List of observer functions
#
#     def subscribe(self, observer):
#         self.observers.append(observer)
#
#     def unsubscribe(self, observer):
#         self.observers.remove(observer)
#
#     def notify(self, data):
#         for observer in self.observers:
#             observer(data)
#
#
# # ConcreteSubject
# class Newsletter(Subject):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def release_new_issue(self, issue_name):
#         print(f'Releasing new issue of {self.name}: {issue_name}')
#         self.notify(issue_name)
#
#     # ConcreteObserver
#     def subscriber1(issue_name):
#         print(f'Subscriber 1 received {issue_name}')
#
#     def subscriber2(issue_name):
#         print(f'Subscriber 2 received {issue_name}')
#
#
# # Usage
# my_newsletter = Newsletter("Python Weekly")
# my_newsletter.subscribe(Newsletter.subscriber1)
# my_newsletter.subscribe(Newsletter.subscriber2)
#
# # Simulating new issue release
# my_newsletter.release_new_issue("Understanding the Event Loop")
#
# from abc import ABC, abstractmethod
#
#
# # Strategy Interface
# class MovementStrategy(ABC):
#     @abstractmethod
#     def move(self, character_name):
#         pass
#
#
# # Concrete Strategies
# class WalkingStrategy(MovementStrategy):
#     def move(self, character_name):
#         print(f'{character_name} is walking.')
#
#
# class RunningStrategy(MovementStrategy):
#     def move(self, character_name):
#         print(f'{character_name} is running.')
#
#
# class TeleportingStrategy(MovementStrategy):
#     def move(self, character_name):
#         print(f'{character_name} just teleported.')
#
#
# class Character:
#     def __init__(self, name, movement_strategy):
#         self.name = name
#         self.movement_strategy = movement_strategy
#
#     def move(self):
#         self.movement_strategy.move(self.name)
#
#     def set_movement_strategy(self, movement_strategy):
#         self.movement_strategy = movement_strategy
#
#
# john = Character("John", WalkingStrategy())
# # Output: John is walking.
# john.move()
#
# john.set_movement_strategy(RunningStrategy())
# # Output: John is running.
# john.move()
#
# john.set_movement_strategy(TeleportingStrategy())
# # Output: John just teleported.
# john.move()

# from abc import ABC, abstractmethod
#
#
# # Receiver
# class Light:
#     def turn_on(self):
#         print("Light turned on")
#
#     def turn_off(self):
#         print("Light turned off")
#
#
# # Command Interface
# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# # Concrete Commands
# class TurnOnCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_on()
#
#
# class TurnOffCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_off()
#
#
# # Invoker
# class RemoteControl:
#     def submit(self, command):
#         command.execute()
#
#
# # Client
# light = Light()
# turn_on_command = TurnOnCommand(light)
# turn_off_command = TurnOffCommand(light)
#
# remote = RemoteControl()
# remote.submit(turn_on_command)  # Output: Light turned on
# remote.submit(turn_off_command)  # Output: Light turned off

# Mediator
# class ChatRoom:
#     def __init__(self):
#         self.users = {}
#
#     def register(self, user):
#         self.users[user.name] = user
#         user.chatroom = self
#
#     def send(self, message, from_user, to_user=None):
#         if to_user:  # Direct message
#             to_user.receive(message, from_user)
#         else:  # Broadcast message
#             for user in self.users.values():
#                 if user != from_user:
#                     user.receive(message, from_user)
#
#
# # Colleague
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.chatroom = None
#
#     def send(self, message, to_user=None):
#         self.chatroom.send(message, self, to_user)
#
#     def receive(self, message, from_user):
#         print(f'{from_user.name} to {self.name}: {message}')
#
#
# # Client code
# chatroom = ChatRoom()
#
# alice = User('Alice')
# bob = User('Bob')
# charlie = User('Charlie')
#
# chatroom.register(alice)
# chatroom.register(bob)
# chatroom.register(charlie)
#
# alice.send('Hi Bob!', bob)
# bob.send('Hey Alice!', alice)
# charlie.send('Hello everyone!')

# Handler
# class Handler:
#     def __init__(self):
#         self.next_handler = None
#
#     def set_next_handler(self, handler):
#         self.next_handler = handler
#
#     def handle(self, request):
#         if self.next_handler:
#             self.next_handler.handle(request)
#
#
# # Concrete Handlers
# class NonEmptyCheck(Handler):
#     def handle(self, request):
#         if request['value'] == '':
#             print('The input cannot be empty.')
#         else:
#             super().handle(request)
#
#
# class NumberCheck(Handler):
#     def handle(self, request):
#         if not isinstance(request['value'], int):
#             print('The input must be a number.')
#         else:
#             super().handle(request)
#
#
# # Client code
# # Try different values here
# input_data = {'value': ''}
#
# non_empty_check = NonEmptyCheck()
# number_check = NumberCheck()
#
# non_empty_check.set_next_handler(number_check)
#
# non_empty_check.handle(input_data)

from abc import ABC, abstractmethod
import math


# # Element
# class Shape(ABC):
#     @abstractmethod
#     def accept(self, visitor):
#         pass
#
#
# # Concrete Elements
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def accept(self, visitor):
#         visitor.visit_circle(self)
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def accept(self, visitor):
#         visitor.visit_rectangle(self)
#
#
# # Visitor
# class ShapeVisitor(ABC):
#     @abstractmethod
#     def visit_circle(self, circle):
#         pass
#
#     @abstractmethod
#     def visit_rectangle(self, rectangle):
#         pass
#
#
# class AreaVisitor(ShapeVisitor):
#     def visit_circle(self, circle):
#         print(f'Area of Circle: {math.pi * circle.radius ** 2}')
#
#     def visit_rectangle(self, rectangle):
#         print(f'Area of Rectangle: {rectangle.width * rectangle.height}')
#
#
# # Client code
# circle = Circle(5)
# rectangle = Rectangle(10, 5)
#
# area_visitor = AreaVisitor()
#
# circle.accept(area_visitor)
# rectangle.accept(area_visitor)


# Memento
# class EditorMemento:
#     def __init__(self, content):
#         self.content = content
#
#     def get_content(self):
#         return self.content
#
#
# # Originator
# class Editor:
#     def __init__(self):
#         self.content = ''
#
#     def type(self, words):
#         self.content += ' ' + words
#
#     def save(self):
#         return EditorMemento(self.content)
#
#     def restore(self, memento):
#         self.content = memento.get_content()
#
#
# # Caretaker
# class Caretaker:
#     def __init__(self):
#         self.mementos = []
#
#     def add_memento(self, memento):
#         self.mementos.append(memento)
#
#     def get_memento(self, index):
#         return self.mementos[index]
#
#
# # Client code
# editor = Editor()
# caretaker = Caretaker()
#
# editor.type('Hello')
# editor.type('World')
#
# caretaker.add_memento(editor.save())
#
# editor.type('!!!')
#
# # Output: Hello World !!!
# print(editor.content)
#
# # Undo
# editor.restore(caretaker.get_memento(0))
# # Output: Hello World
# print(editor.content)

from abc import ABC, abstractmethod


# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


# Terminal Expression
class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


# Nonterminal Expression for Addition
class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Nonterminal Expression for Subtraction
class SubtractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


# Client code
context = {}

# Represents an expression: (1 + (2 - 3))
expression = AddExpression(
    NumberExpression(1),
    SubtractExpression(
        NumberExpression(2),
        NumberExpression(3)
    )
)

# Output: 0
print(expression.interpret(context))