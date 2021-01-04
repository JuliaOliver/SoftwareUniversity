n = int(input())

hit_points_dict = {}
mana_points_dict = {}

for i in range(n):
    hero_input = input().split()
    hero = hero_input[0]
    hit_points = int(hero_input[1])
    mana_points = int(hero_input[2])

    hit_points_dict[hero] = hit_points
    mana_points_dict[hero] = mana_points

while True:
    command_input = input()

    if command_input == "End":
        break

    args = command_input.split(" - ")
    command = args[0]
    hero = args[1]

    if command == "CastSpell":
        mana_needed = int(args[2])
        spell_name = args[3]
        if mana_points_dict[hero] >= mana_needed:
            mana_points_dict[hero] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {mana_points_dict[hero]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(args[2])
        attacker = args[3]
        hit_points_dict[hero] -= damage
        if hit_points_dict[hero] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hit_points_dict[hero]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            hit_points_dict.pop(hero)
            mana_points_dict.pop(hero)

    elif command == "Recharge":
        amount = int(args[2])
        if mana_points_dict[hero] + amount <= 200:
            mana_points_dict[hero] += amount
            print(f"{hero} recharged for {amount} MP!")
        else:
            print(f"{hero} recharged for {200 - mana_points_dict[hero]} MP!")
            mana_points_dict[hero] = 200

    elif command == "Heal":
        amount = int(args[2])
        if hit_points_dict[hero] + amount <= 100:
            hit_points_dict[hero] += amount
            print(f"{hero} healed for {amount} HP!")
        else:
            print(f"{hero} healed for {100 - hit_points_dict[hero]} HP!")
            hit_points_dict[hero] = 100

sorted_hit_dict = dict(sorted(hit_points_dict.items(), key=lambda x: (-x[1], x[0])))

for hero, hit in sorted_hit_dict.items():
    print(hero)
    print(f"  HP: {hit}")
    print(f"  MP: {mana_points_dict[hero]}")
