import math
n = int(input())
k = round(math.log(n, 3))

def empty_space(k):
    ret = []
    for i in range(3 ** (k - 1)):
        ret += [' ' * (3 ** (k - 1))]
    return ret

def sol(k):
    if k == 1:
        return ['***',
                '* *',
                '***']
    else:
        ret = []
        small = sol(k - 1)
        for row in list(zip(small, small, small)):
            ret.append(str(row[0]) + str(row[1]) + str(row[2]))
        for row in list(zip(small, empty_space(k), small)):
            ret.append(str(row[0]) + str(row[1]) + str(row[2]))
        for row in list(zip(small, small, small)):
            ret.append(str(row[0]) + str(row[1]) + str(row[2]))
        return ret

for row in sol(k):
    print(row)
