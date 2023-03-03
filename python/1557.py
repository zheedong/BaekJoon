# Mobius Function
# https://kyr-db.tistory.com/171?category=1008500
# https://ohgym.tistory.com/19
# https://ko.wikipedia.org/wiki/뫼비우스_함수

# Build mu function
MAX_NUM = 42000
mu = [0 for _ in range(MAX_NUM + 10)]
mu[0] = None
mu[1] = 1

for i in range(1, MAX_NUM + 1):
    for j in range(2 * i, MAX_NUM + 1, i):
        mu[j] -= mu[i]

def cound_SFI(n):
    cnt = 0
    i = 1
    while i ** 2 <= n:
        cnt += mu[i] * (n // (i ** 2))
        i += 1 
    return cnt

n = int(input())

# Count Mobius Function
left = 0
right = 2 * n
while left < right - 1:
    mid = (left + right) // 2
    if cound_SFI(mid) < n:
        left = mid
    else:
        right = mid
print(right)
