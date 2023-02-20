from math import log2

n = int(input())
k = int(log2(n // 3))

def add_margin(lst, margin):
    return list(map(lambda x: [' ' * margin] + x + [' ' * margin], lst))

def print_star(k):
    if k == 0:
        return [[' ', ' ', '*', ' ', ' '],
                [' ', '*', ' ', '*', ' '],
                ['*', '*', '*', '*', '*']]
    else:
        bef = print_star(k - 1)
        '''
        k = 0 margin 0
        k = 1 margin 3 ** 1
        k = 2 margin 3 * 2 ** (k - 1)
        k = 3 margin 12
        '''
        return add_margin(bef, 3 * (2 ** (k - 1))) + list(map(lambda x: x[0] + [' '] + x[1], zip(bef, bef)))

for row in print_star(k):
    print(''.join(row))
