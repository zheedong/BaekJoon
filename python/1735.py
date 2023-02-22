from math import gcd
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

up = a2 * b1 + a1 * b2
down = b1 * b2
common = gcd(up, down)
print(up // common, down // common)
