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
    print(search_stack)
    if stack_pop in search_stack:
        continue
    else:
        dfs_searched_node.append(stack_pop)
        search_stack.append(sorted(list(edge[stack_pop])))
        
print(dfs_searched_node)
    