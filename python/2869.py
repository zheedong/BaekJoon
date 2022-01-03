a, b, v = map(int, input().split())

up_per_day = a - b

n_day = (v - a) // up_per_day

while True:
    if up_per_day * n_day + a >= v:
        n_day += 1
        break
    n_day += 1
print(n_day)