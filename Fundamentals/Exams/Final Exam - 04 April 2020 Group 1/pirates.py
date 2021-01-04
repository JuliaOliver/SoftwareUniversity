population = {}
gold = {}
counter = 0

while True:
    first_input = input()

    if first_input == "Sail":
        break

    first_args = first_input.split("||")
    town = first_args[0]
    people = int(first_args[1])
    money = int(first_args[2])

    if town in population and town in gold:
        population[town] += people
        gold[town] += money
        continue

    population[town] = 0
    gold[town] = 0


    population[town] += people
    gold[town] += money
    counter += 1

while True:
    second_input = input()

    if second_input == "End":
        break

    second_args = second_input.split("=>")
    command = second_args[0]
    town = second_args[1]

    if command == "Plunder":
        people = int(second_args[2])
        money = int(second_args[3])
        population[town] -= people
        gold[town] -= money
        print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")
        if population[town] <= 0 or gold[town] <= 0:
            print(f"{town} has been wiped off the map!")
            population.pop(town)
            gold.pop(town)
            counter -= 1

    elif command == "Prosper":
        money = int(second_args[2])
        if money < 0:
            print("Gold added cannot be a negative number!")
            continue
        gold[town] += money
        print(f"{money} gold added to the city treasury. {town} now has {gold[town]} gold.")


if bool(population) and bool(gold):
    sorted_dict = dict(sorted(gold.items(), key=lambda x: (-x[1], x[0])))

    print(f"Ahoy, Captain! There are {abs(counter)} wealthy settlements to go to:")
    for k, v in sorted_dict.items():
        print(f"{k} -> Population: {population[k]} citizens, Gold: {v} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
