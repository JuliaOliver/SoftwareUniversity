targets = input().split()
targets = list(map(int, targets))

input_command = input()

while input_command != "End":
    new_command = input_command.split()
    command = new_command[0]
    index = int(new_command[1])
    value = int(new_command[2])

    if command == "Shoot":
        if 0 <= index <= len(targets) - 1:
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
        # input_command = input()

    elif command == "Add":
        if 0 <= index <= len(targets) -1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

        # input_command = input()

    elif command == "Strike":
        start = index - value
        end = index + value
        if start < 0 or end >= len(targets):
            print("Strike missed!")
            input_command = input()
            continue
        else:
            for i in range(start, end + 1):
                targets.pop(start)

    input_command = input()

targets = list(map(str, targets))
print("|".join(targets))
