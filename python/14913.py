a, d, k = map(int, input().split())

def sol(a, d, k):
    if (k - a) // d == (k - a) / d and ((k - a) // d) + 1 > 0:
        print(((k - a) // d) + 1)
    else:
        print("X")

sol(a, d, k)