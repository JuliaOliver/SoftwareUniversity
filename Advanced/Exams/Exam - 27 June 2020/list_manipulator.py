def list_manipulator(nums_list, *args):
    first_arg = args[0]
    second_arg = args[1]
    if first_arg == "add" and second_arg == "beginning":
        adds = list(args[2:])
        nums_list = adds + nums_list

    elif first_arg == "add" and second_arg == "end":
        adds = list(args[2:])
        nums_list = nums_list + adds

    elif first_arg == "remove" and second_arg == "beginning":
        if len(args) > 2:
            nums_list = nums_list[args[2]:]
        else:
            nums_list = nums_list[1:]

    elif first_arg == "remove" and second_arg == "end":
        if len(args) > 2:
            nums_list = nums_list[:-args[2]]
        else:
            nums_list = nums_list[:-1]

    return nums_list
