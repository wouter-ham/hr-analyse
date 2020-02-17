val = list(filter(lambda x: x > 10, [1, 3, 9, 22, -7, 18]))


def Filter(f, L):
    return [x for x in L if f(x)]


print(Filter(lambda x: x > 10, [1, 3, 9, 22, -7, 18]))

