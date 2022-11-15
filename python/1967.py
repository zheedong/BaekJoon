import sys
from collections import deque
input = sys.stdin.readline

node_num = int(input().rstrip())

adj_dist = [[None] for _ in range(node_num + 1)]

for _ in range(node_num - 1):
    from_node, to_node, weight = map(int, input().split())
    adj_dist[from_node].append((to_node, weight))
    adj_dist[to_node].append((from_node, weight))

'''
tc1_node_num = 12
tc1 = [[None],
       [None, (2, 3), (3, 2)],
       [None, (1, 3), (4, 5)],
       [None, (1, 2), (5, 11), (6, 9)],
       [None, (2, 5), (7, 1), (8, 7)],
       [None, (3, 11), (9, 15), (10, 4)],
       [None, (3, 9), (11, 6), (12, 10)],
       [None, (4, 1)],
       [None, (4, 7)],
       [None, (5, 15)],
       [None, (5, 4)],
       [None, (6, 6)],
       [None], (6, 10)]

tc2_node_num = 5
tc2 = [[None],
       [None, (2, 3), (3, 4), (4, 5), (5, 6)],
       [None, (1, 3)],
       [None, (1, 4)],
       [None, (1, 5)],
       [None, (1, 6)]] 

node_num = tc2_node_num
adj_dist = tc2
'''

# DFS
# 1) 임의의 노드 x에서 가장 먼 거리에 있는 노드 a를 찾는다
# 2) 노드 a에서 가장 먼 거리에 있는 노드 b를 찾는다
# 3) 트리의 지름은 a와 b를 연결하는 통로이다.
# 이렇게 간단한 아이디어를 왜 생각 못 했을까... :(

def get_adj_nodes(node):
    return adj_dist[node][1:]

def dfs(root):
    visited = []
    search_stack = deque([(root, 0)])

    while(search_stack):
        cur_node, cur_path_weight_sum = search_stack.pop()
        if cur_node not in list(map(lambda x : x[0], visited)):
            visited.append((cur_node, cur_path_weight_sum))
            for next in get_adj_nodes(cur_node):
                next_node, next_edge = next
                search_stack.append((next_node, next_edge + cur_path_weight_sum))
    return sorted(visited, key=lambda x:-x[1])

print(dfs(dfs(1)[0][0])[0][1])