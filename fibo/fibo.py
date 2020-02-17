# @memoize
def fibo(n):
    if n <= 1: return n
    return fibo(n - 2) + fibo(n - 1)


def memoize(f):
    fdict = {}

    def f_(*k):
        if k not in fdict:
            fdict[k] = f(*k)
        return fdict[k]

    return f_


fibo = memoize(fibo)


# print(fibo(996))


def test(a, n):
    if n == 1: return a
    return a * test(a, n - 1)


# print(test(5, 3))


def Max(L):
    L = sorted(L)
    return L[len(L) - 1]


# print(Max([3, 7, -7, 22, 8]))


def printNum(n):
    if n > 0:
        n += printNum(n - 1)
    return n


# print(printNum(7))
