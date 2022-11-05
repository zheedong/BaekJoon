import heapq
import sys
input = sys.stdin.readline

def abs(n):
    return n if n >= 0 else -n

n = int(input().rstrip())

abs_heap = []

for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        try:
            print(heapq.heappop(abs_heap)[1])
        except IndexError:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))