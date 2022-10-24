# 0-1 BFS
'''
원래 최단거리라 하면 dijkstra를 써야 함.
문제의 설정상 weight가 0 - 1만 있는 경우 O(V + E) 선형 시간 안에 풀 수 있다.
'''
# https://nicotina04.tistory.com/168
from collections import deque

n, k = map(int, input().split())

INF = 9999999999999
# 문제의 최대 값은 100,000 이지만 2배가 될 수도 있어서 메모리를 넉넉하게 잡아 둔다.
# n에서부터의 최단 거리를 기록해 둔다.
dist = [INF for _ in range(250000)]
dist[n] = 0

search_queue = deque([n])

while search_queue:
    cur_poss = search_queue.popleft()
    if cur_poss == k:
        break
    left_poss, right_poss, warp_poss = cur_poss - 1, cur_poss + 1, cur_poss * 2

    # 새롭게 이동하는 경우가 기존의 거리보다 가까운 경우에만 업데이트 하면서 queue에 넣는다.
    if warp_poss <= 200000 and dist[warp_poss] > dist[cur_poss]:
        dist[warp_poss] = dist[cur_poss]
        # 이동 비용이 0이면 queue 앞에 넣는다.
        search_queue.appendleft(warp_poss)
    if left_poss >= 0 and dist[left_poss] > dist[cur_poss] + 1:
        dist[left_poss] = dist[cur_poss] + 1
        # 이동 비용이 1이면 queue 뒤에 넣는다.
        search_queue.append(left_poss)
    if right_poss <= 200000 and dist[right_poss] > dist[cur_poss] + 1:
        dist[right_poss] = dist[cur_poss] + 1
        search_queue.append(right_poss)

print(dist[k])