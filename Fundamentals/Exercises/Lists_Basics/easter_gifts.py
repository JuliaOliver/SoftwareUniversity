gifts_list = input().split()
command = input()
new_gift = ""
new_list = []
length = str(len(gifts_list))
length = int(length)
none_gift = "None"
list_indexes = length - 1

while command != "No Money":
    new_command = command.split()
    for i in range(length):
        new_list = gifts_list
        if new_command[0] == "OutOfStock":
            new_gift = new_command[-1]
            if new_gift in new_list and new_gift == gifts_list[i]:
                new_list[i] = none_gift
        if new_command[0] == "Required":
            index = int(new_command[-1])
            new_gift = new_command[-2]
            if index > list_indexes or index < 0:
                continue
            elif index == list_indexes:
                new_list[index - 1] = new_gift
            elif index < list_indexes:
                new_list[index] = new_gift
        if new_command[0] == "JustInCase":
            new_gift = new_command[-1]
            new_list[-1] = new_gift
    command = input()

for i in range(length):
    if "None" in new_list:
        new_list.remove("None")

last_list = " ".join(new_list)
print(last_list)
