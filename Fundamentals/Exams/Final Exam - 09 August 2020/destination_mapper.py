import re

string = input()

pattern = r"(=|/)([A-Z][A-Za-z]{2,})(\1)"

matches = re.findall(pattern, string)

destinations = []
travel_points = 0

for match in matches:
    destinations.append(match[1])

for dest in destinations:
    length = len(dest)
    travel_points += length

destinations = ", ".join(destinations)
print(f"Destinations: {destinations}")
print(f"Travel Points: {travel_points}")
