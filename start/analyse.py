# for i in range(1, 101):
#     print(str(i), ('foo' if (i % 3 == 0) else '') + ('bar' if (i % 5 == 0) else ''))
from typing import List

l: List[int] = [i for i in range(1, 20 + 1) if not i % 2]

print(str(l))
