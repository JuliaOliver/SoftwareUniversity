# n = int(input())
# stack = []
#
# for i in range(n):
#     input_command = list(input().split(" "))
#     command = input_command[0]
#
#     if command == "1":
#         char = input_command[1]
#         stack.append(char)
#
#     elif command == "2" and stack:
#         stack.pop()
#
#     elif command == "3":
#         print(max(stack))
#
#     elif command == "4":
#         print(min(stack))
#
# stack = ", ".join(stack)
# print(stack)

n = int(input())

numbers = []

for _ in range(n):
    tokens = input().split()
    command = int(tokens[0])

    if command == 1:
        numbers.append(int(tokens[1]))

    elif command == 2:
        if numbers:
            numbers.pop()

    elif command == 3:
        if numbers:
            print(max(numbers))

    elif command == 4:
        if numbers:
            print(min(numbers))

print(", ".join([str(x) for x in reversed(numbers)]))
