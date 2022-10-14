from itertools import permutations

n, m = map(int, input().split())
inp = map(int, input().split())

for permus in sorted(list(set(permutations(inp, m)))):
    print(*permus)