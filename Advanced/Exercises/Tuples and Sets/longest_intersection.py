n = int(input())

intersection = []

for i in range(n):
    set_1_values, set_2_values = tuple(input().split("-"))

    set_1_start, set_1_end = tuple(set_1_values.split(","))
    set_1 = set(range(int(set_1_start), int(set_1_end) + 1))

    set_2_start, set_2_end = tuple(set_2_values.split(","))
    set_2 = set(range(int(set_2_start), int(set_2_end) + 1))

    set_intersection = set_1 & set_2
    intersection.append(set_intersection)

longest_set = set()

for set_intersection in intersection:
    set_size = len(set_intersection)

    if set_size > len(longest_set):
        longest_set = set_intersection

print(f"Longest intersection is {sorted(list(longest_set))} with length {len(longest_set)}")
