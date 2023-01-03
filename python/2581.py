m = int(input())
n = int(input())

prime_list = []

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for prime in range(2, n + 1):
    if is_prime(prime):
        prime_list.append(prime)

for idx, prime in enumerate(prime_list):
    if prime >= m:
        prime_list = prime_list[idx:]
        break
else:
    prime_list = []


if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])
