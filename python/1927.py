import sys
import heapq        # 11279와 유사

n = int(input())
min_heap = []

for _ in range(n):
    inp = int(sys.stdin.readline())        # Input 양 많을 땐sys input 사용하기
    if inp == 0:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)
    else:
        heapq.heappush(min_heap, inp)