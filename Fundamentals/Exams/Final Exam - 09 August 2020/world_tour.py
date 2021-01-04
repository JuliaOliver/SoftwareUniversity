string = input()

while True:
    input_command = input()

    if input_command == "Travel":
        break

    args = input_command.split(":")
    command = args[0]

    if command == "Add Stop":
        index = int(args[1])
        new_string = args[2]
        if index <= len(string) - 1:
            string = string[:index] + new_string + string[index:]
            
        print(string)

    elif command == "Remove Stop":
        start_index = int(args[1])
        end_index = int(args[2])
        if 0 <= start_index <= len(string)-1 and end_index <= len(string)-1:
            substring = string[start_index:end_index+1]
            string = string.replace(substring, "", 1)
            
        print(string)

    elif command == "Switch":
        old_string = args[1]
        new_string = args[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
            
        print(string)

    else:
        print(string)

print(f"Ready for world tour! Planned stops: {string}")
