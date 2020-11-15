targets = input().split(" ")
targets = list(map(int, targets))
shot_targets = 0
final_list = []

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index >= len(targets):
        continue
    elif targets[index] == -1:
        continue
    else:
        current_num = targets[index]
        for i in range(len(targets)):
            num = targets[i]
            if num == -1:
                continue
            if num > current_num:
                num -= current_num
                targets[i] = num
            elif num <= current_num:
                num += current_num
                targets[i] = num
            if targets[index] != -1:
                targets[index] = -1
                shot_targets += 1

targets = list(map(str, targets))
targets = " ".join(targets)

print(f"Shot targets: {shot_targets} -> {targets}")
