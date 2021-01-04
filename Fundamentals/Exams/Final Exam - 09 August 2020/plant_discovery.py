n = int(input())

rarity_dict = {}
rating_dict = {}

for i in range(n):
    input_plant = input().split("<->")
    plant = input_plant[0]
    rarity = int(input_plant[1])
    rarity_dict[plant] = rarity
    rating_dict[plant] = []

while True:
    input_command = input()
    if input_command == "Exhibition":
        break

    args = input_command.split(": ")
    command = args[0]

    if command == "Rate":
        second_command = args[1]
        new_args = second_command.split(" - ")
        plant = new_args[0]
        if plant not in rarity_dict:
            print("error")
            continue
        rating = int(new_args[1])
        rating_dict[plant].append(rating)

    elif command == "Update":
        second_command = args[1]
        new_args = second_command.split(" - ")
        plant = new_args[0]
        if plant not in rarity_dict:
            print("error")
            continue
        new_rarity = int(new_args[1])
        rarity_dict[plant] = new_rarity

    elif command == "Reset":
        second_command = args[1]
        plant = second_command
        if plant not in rarity_dict:
            print("error")
            continue
        rating_dict[plant].clear()

    else:
        print("error")

average_ratings = []

for v in rating_dict.values():
    summary = 0
    for dig in v:
        summary += dig
    if v == []:
        aver_rate = 0
        average_ratings.append(aver_rate)
        continue
    aver_rate = summary / len(v)
    average_ratings.append(aver_rate)

plants = {}

for k, v in rarity_dict.items():
    plants[k] = {}
    plants[k]["rarity"] = v
    for rate in average_ratings:
        plants[k]["rate"] = rate
        average_ratings.pop(0)
        break

sorted_plants = sorted(plants.keys(), key=lambda c:(-plants[c]["rarity"], -plants[c]["rate"]))

print("Plants for the exhibition:")
for x in sorted_plants:
    print(f"- {x}; Rarity: {plants[x]['rarity']}; Rating: {plants[x]['rate']:.2f}")
