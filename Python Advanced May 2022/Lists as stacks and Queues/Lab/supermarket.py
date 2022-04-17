from collections import deque

clients_queue = deque()
customers = input()
while customers != "End":
    if customers == "Paid":
        for _ in range(len(clients_queue)):
            print(clients_queue.popleft())
    else:
        clients_queue.append(customers)

    customers = input()

print(f"{len(clients_queue)} people remaining.")