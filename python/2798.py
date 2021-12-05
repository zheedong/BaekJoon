# n = 카드의 개수
# m = 목표 숫자
from itertools import combinations
from bisect import bisect_left

def add_tuple_three_element(tup):
    a, b, c = tup
    return a+b+c

n, m = map(int, input().split())

inp_list = list(map(int,input().split()))

possible_comb = sorted(list(set(map(add_tuple_three_element, list(combinations(inp_list, 3))))))

if m in possible_comb:
    print(m)
else:
    print(possible_comb[bisect_left(possible_comb, m) - 1])