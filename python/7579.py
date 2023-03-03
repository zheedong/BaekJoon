import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# dp[ith_app][cur_cost] : Maximum memory up to ith_app as cur_cost
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]
ans = int(1e9)

for ith_app in range(n):
    for cur_cost in range(sum(cost) + 1):
        # Cannot turn off ith_app
        if cost[ith_app] > cur_cost:
            dp[ith_app][cur_cost] = dp[ith_app - 1][cur_cost]
        # Can turn off ith_app
        else:
            # Compar max memory : NOT Turn off vs Turn off + maximum memory with new cost
            dp[ith_app][cur_cost] = max(dp[ith_app - 1][cur_cost], memory[ith_app] + dp[ith_app - 1][cur_cost - cost[ith_app]])

        # If it satisfy condition
        if dp[ith_app][cur_cost] >= m:
            ans = min(ans, cur_cost)

print(ans)