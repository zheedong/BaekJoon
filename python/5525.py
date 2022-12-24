n = int(input())
m = int(input())
ioi_str = input()

p_n = "I" 
p_n += "OI" * n

# O(NM)
def naive_sol():
    cnt = 0
    for idx in range(m - len(p_n)):
        if p_n == str(ioi_str[idx:idx + len(p_n)]):
            cnt += 1
    return cnt

pi_table = [-1, 0, 0, ]

# O(N + M)
def kmp():
    print()