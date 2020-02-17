from functools import lru_cache

import matplotlib.pyplot as plt

mem = lru_cache(maxsize=None)


def valuerange(a: int, b: int, n: int):
    return [a + (b - a) / n * j for j in range(n)]


X = valuerange(-5, 5, 100)
Y = [x * x for x in X]


# plt.plot(X, Y)


# plt.plot([0, 10, 7, 0], [0, 0, 7, 0])

@mem
def P(s: int, d: int):
    if d == 1: return 1 / 6 if (1 <= s <= 6) else 0
    return sum(P(j, 1) * P(s - j, d - 1) for j in range(1, 6 + 1))


X = list(range(3, 18 + 1))
Y = [P(s, 3) for s in X]

for d in range(1, 9 + 1):
    plt.subplot(330 + d)
    X = list(range(d, 6 * d + 1))
    Y = [P(s, d) for s in X]
    plt.bar(X, Y)

plt.show()
