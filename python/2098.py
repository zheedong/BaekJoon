import sys
input = sys.stdin.readline

n = int(input())

adj_mat = []
for _ in range(n):
    adj_mat.append(list(map(int, input().split())))

dp = [[None for _ in range(n)] for _ in range(n)]

for row in adj_mat:
    print(row)

def tsp(start):
    if 
    min_value = int(1e9)
    for j in range(2, n + 1):
        if 