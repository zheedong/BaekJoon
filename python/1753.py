import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input().rstrip())

INF = 3000000

adj_dist = [[None] for _ in range(v + 1)]

for _ in range(e):
    u1, u2, w = map(int, input().split())
    adj_dist[u1].append([u2, w])

is_visited = [False] * (v + 1)
is_visited[0] = None

answer = [INF for _ in range(v + 1)]
answer[0] = None
answer[k] = 0

# Priority queue. heapq 로 구현.
    # [거리, node] 순서로 들어가야 함. [0]이 Priority
dist_end = [[0, k]]

# Dijkstra algorithm
# 이거 푸는데 6시간 걸림
while(dist_end):
    cur_dist, current_node = heapq.heappop(dist_end)
    if is_visited[current_node]:
        continue
    if answer[current_node] < cur_dist:
        continue 
    for next_node, next_weight in adj_dist[current_node][1:]:
        new_dist = cur_dist + next_weight
        if new_dist < answer[next_node]:
            answer[next_node] = new_dist
            heapq.heappush(dist_end, [new_dist, next_node])
    is_visited[current_node] = True

s = ""
for val in answer[1:]:
    s += "INF" if val >= INF else str(val)
    s += "\n"
print(s)