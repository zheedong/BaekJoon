import sys
input = sys.stdin.readline

n = int(input().rstrip())

inp_lst = []
for _ in range(n):
    inp_lst.append(int(input().rstrip()))
inp_lst.sort()

def sol(n):
    global inp_lst
    if n == 1:
        return inp_lst[0] + inp_lst[1]
    return sol(n - 1) + inp_lst[n]