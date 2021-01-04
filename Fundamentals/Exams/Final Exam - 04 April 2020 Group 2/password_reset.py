password_to_change = input()

command = input()

while command != "Done":
    if command == "TakeOdd":
        password_to_change = password_to_change[1:len(password_to_change):2]
        print(password_to_change)

    elif command.split()[0] == "Cut":
        index = int(command.split()[1])
        length = int(command.split()[2])
        remove = password_to_change[index:index + length]
        password_to_change = password_to_change.replace(remove, "", 1)
        print(password_to_change)

    elif command.split()[0] == "Substitute":
        move_out = command.split()[1]
        move_in = command.split()[2]
        if move_out not in password_to_change:
            print("Nothing to replace!")
        else:
            password_to_change = password_to_change.replace(move_out, move_in)
            print(password_to_change)

    command = input()

print(f"Your password is: {password_to_change}")
