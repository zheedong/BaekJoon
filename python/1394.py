char_lst = list(input())
password = list(input())

def mod_sum(a, b, n):
    # (a + b) mod n
    return ((a % n) + (b % n)) % n

def mod_dot(a, b, n):
    # (a * b) mod n
    return ((a % n) * (b % n)) % n

# https://velog.io/@choihocheol/%EB%B9%A0%EB%A5%B8-%EA%B1%B0%EB%93%AD%EC%A0%9C%EA%B3%B1-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98Fast-Exponentiation-Algorithm
# Square and Multiply
# a^9 = a^[1001]_2 = a^8 * 1 * 1 * a
def fast_exponetiation(a, x, n):
    # a^x mod n
    y = 1
    while x > 0:
        if x & 1 == 1:
            y = (a * y) % n
        a = (a * a) % n
        x = x >> 1
    return y

def sol(char_lst, password):
    N = 900528
    ret = 0
    for digit, char in enumerate(reversed(password)):
        ret = mod_sum(ret, mod_dot(fast_exponetiation(len(char_lst), digit, N), (char_lst.index(char) + 1), N), N)
    return ret

print(sol(char_lst, password))