n = int(input())

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

def sum_i_2_j(i, j):
    global prime_lst
    return prime_lst[j + 1] - prime_lst[i]

prime_lst = []
for i in range(2, n + 1):
    if is_prime(i):
        prime_lst.append(i)

for i in range(1, len(prime_lst)):
    prime_lst[i] += prime_lst[i - 1]

prime_lst = [0] + prime_lst


start, end = 0, 0
cnt = 0
while start <= end:
    if start >= len(prime_lst) - 1 or end >= len(prime_lst) - 1:
        break
    elif sum_i_2_j(start, end) < n:
        end += 1
    elif sum_i_2_j(start, end) == n:
        cnt += 1
        end += 1
    else:
        start += 1

print(cnt)
