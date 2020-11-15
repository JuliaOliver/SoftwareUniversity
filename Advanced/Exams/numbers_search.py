def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    missing_num = 0
    for num in args:
        if num == max_num:
            continue
        number = num + 1
        if number not in args:
            missing_num = number

    nums = []
    duplicates = []
    for i in range(len(args)):
        if args[i] in nums:
            if args[i] in duplicates:
                continue
            duplicates.append(args[i])
        nums.append(args[i])

    return [missing_num, sorted(duplicates)]
