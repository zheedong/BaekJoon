N = 1000000007

def mod_sum(a, b):
    # a + b mode N
    return ((a % N) + (b % N)) % N

def mod_dot(a, b):
    # a * b mod N
    return ((a % N) * (b % N)) % N

dp = {0 : 0, 1 : 1}

# F_a+b = F_a-1 * F_b + F_a * F_b+1
# 도가뉴 항등식을 이용
def sol(n):
    if n in dp:
        return dp[n]
    elif n % 2 == 0:
        # F_n = {F_{n / 2 - 1} + (F_{n / 2 - 1} + F_{n / 2})}
        f_1 = sol(n // 2 - 1)
        f = sol(n // 2)
        dp[n] = mod_dot(f, mod_sum(mod_dot(2, f_1), f))
        return dp[n]
    else:
        # F_n = F_{n // 2} * F_{n // 2} + F_{n // 2 + 1} * F_{n // 2 + 1}
        f = sol(n // 2)
        f_p1 = sol(n // 2 + 1)
        dp[n] = mod_sum(mod_dot(f, f), mod_dot(f_p1, f_p1))
        return dp[n]

print(sol(int(input())))