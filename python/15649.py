from itertools import permutations

n, m = map(int, input().split())
for tup in list(permutations(range(1, n + 1), m)):
    print(*list(tup))