def my_func(*args):
    args_list = list(args)
    args_list.sort()

    return args_list[-1] + args_list[-2]


print(my_func(250, 1, 250, 3))
