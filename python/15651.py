from itertools import product

n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]
for ret in list(product(lst, repeat = m)):
    print(*ret)