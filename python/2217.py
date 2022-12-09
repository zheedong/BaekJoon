import sys
input = sys.stdin.readline

n = int(input().rstrip())

lope = []
for _ in range(n):
    lope.append(int(input().rstrip()))
lope.sort(reverse=True)

max_weight = 0
for k in range(1, n + 1):
    cur_max = k * lope[k - 1]
    max_weight = max(max_weight, cur_max)

print(max_weight)