from itertools import combinations

n = map(int, input())

inp_list = list(map(int, input().split()))

ret = 0
for i in range(n, 0, -1):
    if i == 1:
        ret = 1
        break
    possible_case = combinations(inp_list, n)