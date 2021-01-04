n = int(input())

elements = set()

for _ in range(n):
    chem_elements = input().split()
    for element in chem_elements:
        elements.add(element)

for elem in elements:
    print(elem)
