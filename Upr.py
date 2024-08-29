from temp import Stack
from quitues import Queue


class TextEditor:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()

    def type_character(self, char):
        self.stack.push(char)
        self.queue.enqueue(f'Typed {char}')

    def undo(self):
        if not self.stack.is_empty():
            char = self.stack.pop()
            self.queue.enqueue(f'Undone character {char}')
        else:
            print('Nothing to undo')

    def process_actions(self):
        while not self.queue.is_empty():
            action = self.queue.dequeue()
            print(action)


editor = TextEditor()
editor.type_character('a')
editor.type_character('b')
editor.type_character('c')
editor.undo()
editor.process_actions()
