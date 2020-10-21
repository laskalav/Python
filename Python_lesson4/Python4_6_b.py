from itertools import cycle

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cyclinator(iter_list):
    count = 0
    for item in cycle(iter_list):
        if count >= len(iter_list) * 2:
            break
        yield item
        count += 1


print([i for i in cyclinator(num_list)])
