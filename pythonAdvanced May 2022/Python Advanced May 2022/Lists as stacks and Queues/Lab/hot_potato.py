from collections import deque

kids_deque = deque([x for x in input().split()])

toss = int(input())

while kids_deque:
    if len(kids_deque) > 1:
        kids_deque.rotate(-toss)
        print(f"Removed {kids_deque.pop()}")
    else:
        print(f"Last is {kids_deque.pop()}")