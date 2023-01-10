n = int(input())

cur_prime = 2
while n != 1:
    if n % cur_prime == 0:
        print(cur_prime)
        n /= cur_prime
        cur_prime = 2
    else:
        cur_prime += 1
