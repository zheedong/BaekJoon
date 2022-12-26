a, b, c = map(int, input().split())
if b == c:
    print(-1)
else:
    x = a // (c - b) + 1
    print(x if x > 0 else -1)
