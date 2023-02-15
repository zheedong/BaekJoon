from collections import deque

n, m = map(int, input().split())
adj_mat = [[None for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2, distance = map(int, input().split())
    adj_mat[node1][node2] = distance
    adj_mat[node2][node1] = distance

for _ in range(m):
    visited = set()
    start, end = map(int, input().split())
    search_queue = deque([(start, 0)])
    while search_queue:
        cur_node, cur_dist = search_queue.popleft()
        if cur_node in visited:
            continue
        visited.add(cur_node)
        if cur_node == end:
            print(cur_dist)
            break
        for next_node, distance in enumerate(adj_mat[cur_node]):
            if distance is not None:
                search_queue.append((next_node, cur_dist + distance))
