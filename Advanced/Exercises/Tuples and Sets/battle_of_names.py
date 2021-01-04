n = int(input())

odds = set()
evens = set()
odd_sum = 0
even_sum = 0

for i in range(n):
    name = input()
    name_sum = 0
    for ch in name:
        name_sum += ord(ch)

    name_sum = name_sum // (i+1)

    if name_sum % 2 == 0:
        evens.add(name_sum)
    else:
        odds.add(name_sum)

for i in odds:
    odd_sum += i
for i in evens:
    even_sum += i

if odd_sum == even_sum:
    union = odds | evens
    unions = []
    for i in union:
        unions.append(str(i))
    print(", ".join(unions))

elif odd_sum > even_sum:
    difference = odds - evens
    differences = []
    for i in difference:
        differences.append(str(i))
    print(", ".join(differences))

elif even_sum > odd_sum:
    symmetric_difference = evens ^ odds
    symmetric_differences = []
    for i in symmetric_difference:
        symmetric_differences.append(str(i))
    print(", ".join(symmetric_differences))
