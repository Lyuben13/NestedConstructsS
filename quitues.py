from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f'Enqueued {item} to queue')

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.popleft()
            print(f'Dequeued {removed_item} from queue')
            return removed_item
        else:
            print('Queue is empty')
            return None

    def front(self):
        if not self.is_empty():
            print(f'Front element is {self.queue[0]}')
            return self.queue[0]
        else:
            print('Queue is empty')
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def task_scheduler(tasks: list):
    queue = Queue()

    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty():
        current_task = queue.dequeue()
        if current_task:
            print(f'Processing task: {current_task}')


def supermarket_checkout(customer: list):
    queue = Queue()

    for customer in customer:
        queue.enqueue(customer)

    while not queue.is_empty():
        processed_customer = queue.dequeue()
        if processed_customer:
            print(f'Processing customer: {processed_customer}')


# customers = ["Customer 1", "Customer 2", "Customer 3"]
# supermarket_checkout(customers)
# customers = ["Customer A", "Customer B", "Customer C", "Customer D", "Customer E"]
# supermarket_checkout(customers)
# customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
# supermarket_checkout(customers)
#
# # tasks = ['Task1', 'Task2', 'Task3']
# # task_scheduler(tasks)
