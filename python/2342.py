import sys
sys.setrecursionlimit(int(1e9))

instructions = list(map(int, input().split()))

left_foot = 0
right_foot = 0

power_mat = [[None for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i == 0:
            if j == 0:
                power_mat[i][j] = 1
            else:
                power_mat[i][j] = 2
        else:
            if j == 0:
                power_mat[i][j] = 0
            elif i == j:
                power_mat[i][j] = 1
            elif abs(i - j) == 2:
                power_mat[i][j] = 4
            else:
                power_mat[i][j] = 3

dp = [[[None for _ in range(len(instructions))] for _ in range(5)] for _ in range(5)]

def sol(left_foot, right_foot, idx):
    global instructions
    if dp[left_foot][right_foot][idx] is not None:
        return dp[left_foot][right_foot][idx]
    else:
        if idx == len(instructions) - 1:
            dp[left_foot][right_foot][idx] = min(power_mat[left_foot][instructions[idx]], power_mat[right_foot][instructions[idx]])
            return dp[left_foot][right_foot][idx]
        else:
            dp[left_foot][right_foot][idx] = \
                min(power_mat[left_foot][instructions[idx]] + sol(instructions[idx], right_foot, idx + 1),
                power_mat[right_foot][instructions[idx]] + sol(left_foot, instructions[idx], idx + 1))
            return dp[left_foot][right_foot][idx]

print(sol(0, 0, 0))
