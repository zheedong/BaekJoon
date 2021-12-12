from collections import deque

number_of_comp = int(input())
number_of_edge = int(input())

# Data Structure : {1 : set[2,3], 2 : set[3, 4], ...}
# 연결된 node들을 저장

connect_node = dict([])

for i in range(1, number_of_comp + 1):
    connect_node[i] = set([])

for i in range(number_of_edge):
    node1, node2 = map(int, input().split())
    connect_node[node1].add(node2)
    connect_node[node2].add(node1)
    
search_queue = deque([1])
searched_node = set([])

while search_queue:
    node_deq = search_queue.popleft()
    
    if node_deq not in searched_node:
        for node in connect_node[node_deq]:
            search_queue.append(node)
    
    searched_node = searched_node.union([node_deq])
    
print(len(searched_node) - 1)