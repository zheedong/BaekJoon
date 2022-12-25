t = int(input())
def is_palindrom(n, depth):
    if len(n) == 1 or len(n) == 0:
        return 1, depth + 1
    elif n[0] != n[-1]:
        return 0, depth + 1
    else:
        return is_palindrom((n[1:-1]), depth + 1)

for _ in range(t):
    print(*is_palindrom(list(input()), 0))