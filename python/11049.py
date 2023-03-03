import sys
input = sys.stdin.readline

n = int(input())

mat_lst = []
for _ in range(n):
    p_x_1, p_x = map(int, input().split())
    mat_lst.append(p_x_1)
mat_lst.append(p_x)

dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][i] = 0

def sol(i, j):
    global mat_lst, dp

    if dp[i][j] is not None:
        return dp[i][j]

    min_val = int(1e9)

    for k in range(i, j):
        min_val = min(min_val, sol(i, k) + sol(k + 1, j) + mat_lst[i - 1] * mat_lst[k] * mat_lst[j])

    dp[i][j] = min_val
    return dp[i][j]

print(sol(1, n))
