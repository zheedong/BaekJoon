from itertools import permutations

n, m = map(int, input().split())

inp_list = list(map(int, input().split()))

res = sorted(list(permutations(inp_list, m)))

for out in res:
    for num in out:
        print(num, end = " ")
    print()