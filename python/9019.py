import sys
from collections import deque

input = sys.stdin.readline

# Save history as integer not str. Because of excution speed.
D = 1
S = 2
L = 3
R = 4

def sol(start, target):
    search_queue = deque([(start, 0)])
    visited = set([])
    while search_queue:
        cur_n, history = search_queue.popleft()
        if cur_n in visited:
            continue
        visited.add(cur_n)
        if cur_n == target:
            return history

        # D
        d_n = (2 * cur_n) % 10000
        search_queue.append((d_n, history * 10 + D))

        # S
        s_n = cur_n - 1
        if s_n == -1:
            s_n = 9999
        search_queue.append((s_n, history * 10 + S))

        # L
        l_n = (cur_n * 10) % 10000 + (cur_n * 10) // 10000
        search_queue.append((l_n, history * 10 + L))

        # R
        r_n = cur_n // 10 + 1000 * (cur_n % 10)
        search_queue.append((r_n, history * 10 + R))

t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().split())
    for ans in str(sol(a, b)):
        if int(ans) == D:
            print("D", end="")
        elif int(ans) == S:
            print("S", end="")
        elif int(ans) == L:
            print("L", end="")
        elif int(ans) == R:
            print("R", end="")
    print()