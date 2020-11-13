import sys
first_list = input()
num = int(input())

new_list = first_list.split()
min_size = sys.maxsize

removal = ""
last_list = ""

for j in range(num):
    smallest = min_size
    for i in new_list:
        if int(i) < smallest:
            smallest = int(i)
            removal = str(smallest)
    new_list.remove(removal)

last_list = ", ".join(new_list)
print(f"[{last_list}]")
