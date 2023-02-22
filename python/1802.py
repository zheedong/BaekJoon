import sys
input = sys.stdin.readline

def xor(a, b):
    if a != b:
        return True
    else:
        return False

def change(lst):
    ret = []
    for val in lst:
        if val == 0:
            ret.append(1)
        else:
            ret.append(0)
    return list(reversed(ret))

def sol(lst):
    if len(lst) == 1:
        return True
    else:
        mid = (len(lst)) // 2
        sub1 = lst[:mid]
        sub2 = lst[mid + 1:]
        if change(sub1) == sub2:
            return sol(sub1)
        else:
            return False

T = int(input().rstrip())
for _ in range(T):
    if sol(list(map(int, list(input().rstrip())))):
        print("YES")
    else:
        print("NO")
