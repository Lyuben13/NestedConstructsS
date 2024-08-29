from collections import deque


def rotate_list(lst: list, n: int):
    dq = deque(lst)
    dq.rotate(n)
    return list(dq)


nums_list = [1, 2, 3, 4, 5, 6]
print(rotate_list(nums_list, 2))
print(rotate_list(nums_list, 3))
print(rotate_list(nums_list, -3))
