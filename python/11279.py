import sys
import heapq            # Heap 자료구조
                        # 1927 문제와 유사

n = int(input())
max_heap = []

for _ in range(n):
    inp = int(sys.stdin.readline())        # Input이 많을 때는 sys input 사용해주기!
    if inp == 0:
        try:
            print(-heapq.heappop(max_heap))        # heapq가 최소 힙이가 때문에 -를 붙여 Max heap으로 응용
        except:
            print(0)
    else:
        heapq.heappush(max_heap, -inp)