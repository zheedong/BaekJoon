def sol(dp, n):
    if n == 1:
        return 0
    else:
        try:
            return dp[n]
        except:
            tower1 = n // 2
            tower2 = n - n // 2
            cur_exciting = tower1 * tower2 
            dp[n] = cur_exciting + sol(dp, tower1) + sol(dp, tower2)
            return dp[n]

n = int(input())
dp = dict([])
print(sol(dp, n))