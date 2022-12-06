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
        # 절댓값 힙. tuple의 [0], [1] 순으로 우선순위가 정해진다.
        heapq.heappush(abs_heap, (abs(x), x))