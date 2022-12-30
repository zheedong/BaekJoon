import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
edge_heap = []

for _ in range(e):
    node1, node2, edge = map(int, input().split())
    heapq.heappush(edge_heap, (edge, node1, node2))


def check_all_visited(visited_node):
    for node in visited_node:
        if not node:
            return False
    else:
        return True


# Prim is too slow.
def prim(edge_heap):
    visited_node = [False for _ in range(v + 1)]
    visited_node[0] = True      # Not used 0 node.

    # Init
    edge, node1, node2 = heapq.heappop(edge_heap)
    min_distance = edge
    visited_node[node1] = visited_node[node2] = True

    while not check_all_visited(visited_node):
        edge, node1, node2 = heapq.heappop(edge_heap)
        not_visited = []
        while not visited_node[node1] ^ visited_node[node2]:
            not_visited.append((edge, node1, node2))
            edge, node1, node2 = heapq.heappop(edge_heap)
        min_distance += edge
        visited_node[node1] = visited_node[node2] = True
        for val in not_visited:
            heapq.heappush(edge_heap, val)
    return min_distance


# Union-Find algorithm
# https://velog.io/@kimdukbae/크루스칼-알고리즘-Kruskal-Algorithm
parent = [i for i in range(v + 1)]
parent[0] = None       # Not used


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    parent[root_y] = root_x


def kruskal(edge_heap):
    edges = sorted(edge_heap)
    min_distance = 0

    for edge in edges:
        edge_dist, node1, node2 = edge
        if find(parent, node1) != find(parent, node2):
            union(parent, node1, node2)
            min_distance += edge_dist
    return min_distance


print(kruskal(edge_heap))
