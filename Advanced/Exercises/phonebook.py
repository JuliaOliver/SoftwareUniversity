is_finished = False

num_names = 0

address_book = {}

while not is_finished:
    next_input = input()


    if next_input.isdigit():
        num_names = int(next_input)
        is_finished = True

    else:
        name, phone = next_input.split("-")
        address_book[name] = phone

for i in range(num_names):
    name_to_check = input()
    if name_to_check in address_book:
        print(f"{name_to_check} -> {address_book[name_to_check]}")
    else:
        print(f"Contact {name_to_check} does not exist.")
