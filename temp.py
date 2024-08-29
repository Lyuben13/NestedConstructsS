class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f'Pushed {item} onto stack')

    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f'Popped {removed_item} from stack')
            return removed_item
        else:
            print('Stack is empty')
            return None

    def peek(self):
        if not self.is_empty():
            print(f'Top element is {self.stack[-1]}')
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def reverse_string(input_str):
    stack = Stack()
    for char in input_str:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or \
                    (char == '}' and top != '{') or \
                    (char == ']' and top != '['):
                return False

    return stack.is_empty()

#
# my_string = reverse_string('Hello, World!')
# print(my_string)

# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.peek()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()

# “(){}[]”
# “[({})]”
# “({[()]})”
# “({[}])”
# “(((())))”
# “([)]”
# “{[()()]}”
# “[(])”
# “{{{{[[[]]]]}}}”
# “{{[[(())]]}}”
# “([{}])({})”
# “{{[[(())]]]}”

# print(is_balanced('{{[[(())]]]}'))



