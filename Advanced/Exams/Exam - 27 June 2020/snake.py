def is_valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size


n = int(input())

matrix = []
snake_pos = []
food_quantity = 0
directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == "S":
            snake_pos = [row, col]
    matrix.append(line)

while True:
    command = input()
    dir_changes = directions[command]
    new_pos = [snake_pos[0] + dir_changes[0], snake_pos[1] + dir_changes[1]]

    if is_valid(new_pos, n):
        matrix[snake_pos[0]][snake_pos[1]] = "."
        element = matrix[new_pos[0]][new_pos[1]]
        if element == "*":
            food_quantity += 1

        elif element == "B":
            matrix[new_pos[0]][new_pos[1]] = "."
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == "B" and matrix[i][j] != new_pos:
                        new_pos = [i, j]

        snake_pos = new_pos
        matrix[snake_pos[0]][snake_pos[1]] = "S"

    if not is_valid(new_pos, n):
        matrix[snake_pos[0]][snake_pos[1]] = "."
        print("Game over!")
        break

    if food_quantity >= 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")
[print("".join(row)) for row in matrix]
