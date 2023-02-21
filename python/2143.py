from collections import Counter

T = int(input())
n = int(input())
a_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))

def sum_lst(i, j, lst):
    return lst[j + 1] - lst[i]

for idx in range(1, n):
    a_lst[idx] = a_lst[idx] + a_lst[idx - 1]
a_lst = [0] + a_lst

for idx in range(1, m):
    b_lst[idx] = b_lst[idx] + b_lst[idx - 1]
b_lst = [0] + b_lst
res = 0
c = Counter()

for start in range(n):
    for end in range(start, n):
        c[sum_lst(start, end, a_lst)] += 1

for start in range(m):
    for end in range(start, m):
        cur_t = T - sum_lst(start, end, b_lst)
        res += c[cur_t]

print(res)