def mod_sum(lst):
    ret = 0
    for val in lst:
        ret = mod_add(ret, val)
    return ret

def mod_add(a, b):
    N = 1000000000
    return (a % N + b % N) % N

n, k = map(int, input().split())

dp = [[1 for _ in range(n + 1)]]
for _ in range(k - 2):
    dp.append([None for _ in range(n + 1)])

# f(n, k) = sum_(i is 0 to n) f(n - i, k - 1)
# O(2nk)
for i in range(1, k - 1):
    dp[i][n] = mod_sum(dp[i - 1][:n + 1])
    # mod_sum is O(n). So just use once.
    for j in reversed(range(n)):
        # O(1)
        dp[i][j] = mod_add(dp[i][j + 1], - dp[i - 1][j + 1])

# Initial case
if k == 1:
    print(1)
else:
    print(mod_sum(dp[k - 2]))