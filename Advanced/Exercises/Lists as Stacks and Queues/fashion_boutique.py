clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())

sum_of_clothes = 0
racks_count = 1

while clothes_in_box:
    cloth = clothes_in_box.pop()
    sum_of_clothes += cloth
    if rack_capacity >= sum_of_clothes:
        if rack_capacity == sum_of_clothes:
            sum_of_clothes = 0
            racks_count += 1
            if not clothes_in_box:
                racks_count -= 1
        continue
    else:
        sum_of_clothes = 0
        clothes_in_box.append(cloth)
        racks_count += 1

print(racks_count)
