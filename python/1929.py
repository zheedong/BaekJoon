import math
m, n = map(int, input().split())

prime_list = [2]

for i in range(3, n):
    flag = True
    for prime in prime_list:
        if i % prime == 0:
            flag = False
            break
    if flag:
        prime_list.append(i)
        
for prime in prime_list:
    if prime >= m and prime <= n:
        print(prime)