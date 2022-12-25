def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 2) + fibb(n - 1)

n = int(input())
print(fibb(n))