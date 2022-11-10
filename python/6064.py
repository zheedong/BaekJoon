import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    if m < n:
        idx = y
        cur_x = y % m
        cur_x = cur_x if cur_x != 0 else m
        is_found = False

        while idx <= math.lcm(m, n):
            if cur_x == x:
                is_found = True
                break
            idx += n
            cur_x += (n - m)
            cur_x %= m
            cur_x = cur_x if cur_x != 0 else m
        if is_found:
            my_sol = idx
        else:
            my_sol = -1
    else:
        idx = x
        cur_y = x % n
        cur_y = cur_y if cur_y != 0 else n
        is_found = False

        while idx <= math.lcm(m, n):
            if cur_y == y:
                is_found = True
                break
            idx += m
            cur_y += (m - n)
            cur_y %= n
            cur_y = cur_y if cur_y != 0 else n
        if is_found:
            my_sol = idx
        else:
            my_sol = -1
    print(my_sol)

# navie solution
def get_all_poss_years(m, n):
    ret = []
    x, y = (1, 1)
    while(True):
        ret.append((x, y))
        if x == m and y == n:
            return ret
        x = x + 1 if x < m else 1
        y = y + 1 if y < n else 1

def naive_solution(m, n, x, y):
    try:
        return get_all_poss_years(m, n).index((x, y)) + 1
    except ValueError:
        return -1
            
'''
최소 공배수 : 마지막 해
math.lcm(m, n)
y = 1
1 : (1, 1)
1 + 12 : (1 + 2, 1)
13 + 12 : (3 + 2, 1)
25 + 12 : (5 + 2, 1)
37 + 12 : (7 + 2, 1)

y = 2
2 : (2, 2)
2 + 12 : (2 + (12 - 10), 2)
2 + 12 + 12 : (2 + (12 - 10) + (12 - 10), 2)

예외 처리 때문에 골치 아팠다...
'''