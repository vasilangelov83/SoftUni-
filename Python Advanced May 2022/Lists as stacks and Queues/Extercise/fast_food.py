from collections import deque

total_food = int(input())

orders_queue = deque([int(x) for x in input().split()])

biggest_order = max(orders_queue)
print(biggest_order)
while orders_queue:
    current_order = orders_queue[0]
    if current_order <= total_food:
        orders_queue.popleft()
        total_food -= current_order
    else:
        break
if not orders_queue:
    print("Orders complete")
else:
    orders_queue = [str(x) for x in orders_queue]
    print(f"Orders left: {' '.join(orders_queue)}")