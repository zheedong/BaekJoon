import sys
inpput = sys.stdin.readline

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

prime_lst = []
for num in range(2, int(1e6)):
    if is_prime(num):
        prime_lst.append(num)
prime_set = set(prime_lst)

inp = None
while inp != 0:
    inp = int(input().rstrip())
    if inp == 0:
        break
    for cur_prime in prime_lst:
        if inp - cur_prime in prime_set:
            print(f"{inp} = {cur_prime} + {inp - cur_prime}")
            break
    else:
        print("Goldbach's conjecture is wrong.")