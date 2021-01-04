n = int(input())

unique_username = set()

for i in range(n):
    name = input()
    unique_username.add(name)

for username in unique_username:
    print(username)
