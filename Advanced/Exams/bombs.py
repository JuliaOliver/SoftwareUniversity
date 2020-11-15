from collections import deque

bomb_effects = [int(x) for x in input().split(", ")]
bomb_casings = [int(x) for x in input().split(", ")]
bomb_effects = deque(bomb_effects)

bombs = {"Datura Bombs":0, "Cherry Bombs":0, "Smoke Decoy Bombs":0}
# Datura Bombs: 40
# Cherry Bombs: 60
# Smoke Decoy Bombs: 120

while True:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    result = effect + casing
    if result == 40:
        bombs["Datura Bombs"] += 1
    elif result == 60:
        bombs["Cherry Bombs"] += 1
    elif result == 120:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        casing -= 5
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing)

    if len(bomb_effects) <= 0 \
        or len(bomb_casings) <= 0 \
        or bombs["Datura Bombs"] >= 3 \
        and bombs["Cherry Bombs"] >= 3 \
        and bombs["Smoke Decoy Bombs"] >= 3:
        break

if bombs["Datura Bombs"] >= 3 \
        and bombs["Cherry Bombs"] >= 3 \
        and bombs["Smoke Decoy Bombs"] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) <= 0:
    print("Bomb Effects: empty")
else:
    effects_list = [x for x in bomb_effects]
    effects = ", ".join(map(str, effects_list))
    print(f"Bomb Effects: {effects}")

if len(bomb_casings) <= 0:
    print("Bomb Casings: empty")
else:
    casings = ", ".join(map(str, bomb_casings))
    print(f"Bomb Casings: {casings}")

for k, v in sorted(bombs.items()):
    print(f"{k}: {v}")
