from collections import deque


class BrowserHistory:
    def __init__(self):
        self.history = deque()
        self.forward_stack = deque()

    def visit(self, page):
        self.history.append(page)
        self.forward_stack.clear()
        print(f'Visited {page}')

    def back(self):
        if len(self.history) > 1:
            current_page = self.history.pop()
            self.forward_stack.appendleft(current_page)
            print(f'Back to:{self.history[-1]}')
        else:
            print('No more pages to go back to')

    def forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.popleft()
            self.history.append(next_page)
            print(f'Forward to: {next_page}')

        else:
            print('No more pages to go forward to')


browser_history = BrowserHistory()
browser_history.visit('google.com')

