number = int(input())

num_range = int(number / 2 + 1)
new_num = 0

for i in range(1, num_range):
    if number % i == 0:
        new_num += i

if new_num == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
