import math
from operator import is_
m, n = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if (n % i) == 0:
            return False
    return True

for num in range(m, n+1):
    if is_prime(num):
        print(num)