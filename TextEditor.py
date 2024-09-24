from collections import deque


class TextEditor:
    def __init__(self):
        self.text = deque()
        self.undo_stack = deque()

    def type_char(self, char):
        self.text.append(char)
        self.undo_stack.clear()
        print(f'Typed: {char}')

    def undo(self):
        if self.text:
            last_char = self.text.pop()
            self.undo_stack.append(last_char)
        else:
            print(f'Nothing to undo')

    def redo(self):
        if self.undo_stack:
            char = self.undo_stack.pop()
            self.text.append(char)
            print(f'Redo: {char}')

        else:
            print('Nothing to redo')

    def display_text(self):
        print(f'Current text:', ''.join(self.text))


editor = TextEditor()
editor.type_char('H')
editor.type_char('e')
editor.type_char('l')
editor.type_char('l')
editor.type_char('o')
editor.type_char('!')
editor.undo()
editor.redo()
editor.display_text()


