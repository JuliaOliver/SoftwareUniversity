from collections import deque

customers_list = deque(int(x) for x in input().split(", "))
taxis_list = [int(x) for x in input().split(", ")]
total_time = 0

while True:
    if customers_list:
        customer = customers_list.popleft()
    if taxis_list:
        taxi = taxis_list.pop()

    if customer <= taxi:
        total_time += customer

    else:
        customers_list.appendleft(customer)

    if len(customers_list) == 0:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
        break

    if len(taxis_list) == 0 and len(customers_list) > 0:
        print("Not all customers were driven to their destinations")
        customers_list = [str(x) for x in customers_list]
        print(f"Customers left: {', ' .join(customers_list)}")
        break
