prime = set([])
not_prime = set([])

def is_prime(n):
    global prime
    global not_prime
    if n == 1:
        return False
    elif n in prime:
        return True
    elif n in not_prime:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                not_prime.add(n)
                return False
        else:
            prime.add(n)
            return True

def bertrand(n):
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            cnt += 1
    return cnt

inp = int(input())
while not inp == 0:
    print(bertrand(inp))
    inp = int(input())