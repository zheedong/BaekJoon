import sys
from collections import deque

input = sys.stdin.readline

def get_right_most(n):
    return int(str(n)[-1])

def get_removed_right(n):
    return int(str(n)[:-1])

def use_only_plus_minus(n):
    return max(n - 100, 100 - n)

def get_digit(n):
    return len(str(n))

# BFS
n = int(input().rstrip())
m = int(input().rstrip())

if m != 0:
    broken_num = list(map(int, input().split()))
else:
    broken_num = []

queue = deque([(n, 1)])
cur_min_digit = get_digit(n)

while queue:
    cur_num, cur_depth = queue.popleft()

    if get_digit(cur_num) > cur_min_digit:
        continue
    elif get_digit(cur_num) < cur_min_digit:
        cur_min_digit = get_digit(cur_num)

    if get_right_most(cur_num) not in broken_num:
        if cur_min_digit == 1:
            break
        queue.append((get_removed_right(cur_num), cur_depth + 1))
    if cur_num != 0:
        queue.append((cur_num - 1, cur_depth + 1))
    queue.append((cur_num + 1, cur_depth + 1))

print(min(use_only_plus_minus(n), cur_depth))