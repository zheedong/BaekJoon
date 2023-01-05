import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edge_heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edge_heap, (c, a, b))

parents = [i for i in range(n + 1)]
parents[0] = None

def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    parents[root_y] = root_x


max_distance = -1

def kruskal(edge_heap):
    global max_distance
    edges = sorted(edge_heap)
    min_distance = 0

    for edge in edges:
        edge_dist, node1, node2 = edge
        if find(parents, node1) != find(parents, node2):
            union(parents, node1, node2)
            min_distance += edge_dist
            max_distance = max(max_distance, edge_dist)
    return min_distance

print(kruskal(edge_heap) - max_distance)
