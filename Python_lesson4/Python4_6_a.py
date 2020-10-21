from itertools import count


def generator(start):
    for i in count(start):
        if i > start + 10:
            break
        else:
            yield i


print([i for i in generator(10)])
