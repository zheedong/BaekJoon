# BFS
import sys
from collections import deque
input = sys.stdin.readline

def bfs(root, adj_mat, n):
    search_queue = deque([root])
    visitied = [False] * (n + 1)
    visitied[0] = None
    airline_cnt = -1
    while search_queue:
        cur_node = search_queue.popleft()
        if visitied[cur_node] == True:
            continue
        visitied[cur_node] = True
        next_nodes = adj_mat[cur_node][1:]
        search_queue.extend(next_nodes)
        airline_cnt += 1
    return airline_cnt

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().split())
    adj_mat = [[None] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj_mat[a].append(b)
        adj_mat[b].append(a)
    # [[None], [None, 2, 3], [None, 1, 3], [None, 2, 1]]

    print(bfs(1, adj_mat, n))