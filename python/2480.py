a, b, c = map(int, input())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    print(1000 + 100 * (a if (a == b or a == c) else b))
else:
    print(max([a, b, c]) * 100)