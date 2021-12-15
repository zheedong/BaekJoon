from collections import deque

n, m, v = map(int, input().split())

node = set([i for i in range(1, n + 1)])
edge = dict([])

for cur_node in range(1, n + 1):
    edge[cur_node] = set([])

for _ in range(m):
    node1, node2 = map(int, input().split())
    edge[node1].add(node2)
    edge[node2].add(node1)
    
search_queue = deque([v])
search_stack = deque([v])

# DFS
dfs_searched_node = []
while search_stack:
    stack_pop = search_stack.pop()
    if stack_pop in dfs_searched_node:
        continue
    else:
        dfs_searched_node.append(stack_pop)
        reversed_node = reversed(sorted(edge[stack_pop]))
        for node in reversed_node:
            search_stack.append(node)
        
# BFS
bfs_searched_node = []
while search_queue:
    queue_pop = search_queue.popleft()
    if queue_pop in bfs_searched_node:
        continue
    else:
        bfs_searched_node.append(queue_pop)
        edges = sorted(edge[queue_pop])
        for node in edges:
            search_queue.append(node)
        
for i in dfs_searched_node:
    print(i, end = " ")
print()
for j in bfs_searched_node:
    print(j, end = " ")