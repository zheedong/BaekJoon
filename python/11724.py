from collections import deque

n, m = map(int, input().split())

edges = dict([])
for i in range(1, n+1):
    edges[i] = set([])

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].add(v)
    edges[v].add(u)
    
# BFS
not_checked_yet = set([i for i in range(1, n + 1)])
connected_component = 0

while not_checked_yet:
    connected_component += 1
    search_queue = deque([list(not_checked_yet)[0]])
    searched_node = set([])

    while search_queue:
        queue_pop = search_queue.popleft()
        if queue_pop in searched_node:
            continue
        else:
            searched_node.add(queue_pop)
            for node in edges[queue_pop]:
                search_queue.append(node)
    not_checked_yet = not_checked_yet.difference(searched_node)
    
print(connected_component)