def self_num(n):
    return n + sum(map(int, str(n)))

is_self = [True for _ in range(20000)]

for i in range(10000):
    is_self[self_num(i + 1)] = False

for i in range(10000):
    if is_self[i + 1] == True:
        print(i + 1)