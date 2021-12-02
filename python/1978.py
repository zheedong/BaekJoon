'''
4
1 3 5 7
'''

import math

def is_prime(target):
    if(target == 1):
        return False
    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i == 0:
            return False
    return True

N = int(input())
inp_int_list = list(map(int, input().split()))

count = 0
for i in range(0, N):
    if is_prime(inp_int_list[i]):
        count += 1
print(count)