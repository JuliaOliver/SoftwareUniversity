# from collections import deque
#
# total_quantity = int(input())
#
# orders_queue = deque(map(int, input().split(" ")))
#
# print(max(orders_queue))
#
# while orders_queue:
#     order = orders_queue.popleft()
#
#     if total_quantity >= order:
#         total_quantity -= order
#     else:
#         orders_queue.appendleft(order)
#         break
#
# if orders_queue:
#      orders_left = " ".join(list(map(lambda x: str(x), orders_queue)))
#      print(f"Orders left: {orders_left}")
# else:
#     print("Orders complete")

from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
success = True

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        success = False
        orders.appendleft(current_order)
        break

if success:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
