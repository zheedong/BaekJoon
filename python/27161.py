# Board Game Cup C

import sys
input = sys.stdin.readline

n = int(input().rstrip())
cur_time = 1
is_reversed = False

for _ in range(n):
    clock_type, clock_time = input().split()
    clock_time = int(clock_time)

    if cur_time == clock_time and clock_type != "HOURGLASS":
        print(f"{cur_time} YES")
    else:
        print(f"{cur_time} NO")

    if clock_type == "HOURGLASS" and cur_time != clock_time:
        is_reversed = not is_reversed

    cur_time = cur_time + (-1 if is_reversed else 1)
    if cur_time == 13:
        cur_time = 1
    if cur_time == 0:
        cur_time = 12
