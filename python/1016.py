# Mobius Function
# https://kyr-db.tistory.com/171?category=1008500
# https://ohgym.tistory.com/19
# https://ko.wikipedia.org/wiki/뫼비우스_함수

# Build mu function
MAX_NUM = int(1e6)
mu = [0 for _ in range(MAX_NUM + 10)]
mu[0] = None
mu[1] = 1

for i in range(1, MAX_NUM + 1):
    for j in range(2 * i, MAX_NUM + 1, i):
        mu[j] -= mu[i]

def count_SFI(n):
    cnt = 0
    i = 1
    while i ** 2 <= n:
        cnt += mu[i] * (n // (i ** 2))
        i += 1 
    return cnt

min_n, max_n = map(int, input().split())
print(count_SFI(max_n) - count_SFI(min_n - 1))
