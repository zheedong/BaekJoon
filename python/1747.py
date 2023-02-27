n = int(input())

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True

def check_palindrom(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-(i+1)]: 
            return False
    else:
        return True

while True:
    if check_palindrom(n) and is_prime(n):
        print(n)
        break
    n += 1