import sys
input = sys.stdin.readline

k, h, q = map(int, input().split())

# White path start from 1
def get_white_path(black):
    print()

def get_same_parent(a, b):
    res = None
    a_white = get_white_path(a)
    b_white = get_white_path(b)
    for idx in range(min(len(a_white), len(b_white))):
        if a_white[idx] != b_white[idx]:
            res = a_white[idx - 1]
            break
    else:
        res = a_white[idx]
    return res

def get_height(white, black):
    return 

def sol(a, b):
    same_parent = get_same_parent(a, b)
    get_height(same_parent, a) + get_height(same_parent, b)

for _ in range(q):
    a, b = map(int, input().split())
    print(sol(a, b))

def get_while_num(k, h):
    res = 0
    for r in range(h):
        res += (k + 1) ** r
    return res

'''
1
2 3 4
5 6 7 8 9 10 11 12 13
'''