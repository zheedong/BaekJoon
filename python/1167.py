# Similar to 1967 
from collections import deque
import sys
input = sys.stdin.readline

def divide_tuple_list(n, lst):
    return list(map(lambda x : x[n], lst))

# You don't need to worry about duplicated input.
def get_input():
    v = int(input().rstrip())
    adj_list = [[None] for _ in range(v + 1)]

    for _ in range(v):
        inp = list(map(int, input().split()))
        vertex_num = inp[0]
        for idx in range(1, len(inp), 2):
            cur_dest = inp[idx]
            if cur_dest == -1:
                break
            cur_dist = inp[idx + 1]
            adj_list[vertex_num].append((cur_dest, cur_dist))

    return adj_list

def dfs(root, adj_list):
    # Time Complexity issue. Search in Set is O(1), but in List is O(n)
    visitied = set([])
    # Save the tuple of node and accumulative sum.
    ret = []

    search_stack = deque([(root, 0)])

    while search_stack:
        cur_node, cur_accumulative_sum = search_stack.pop()
        # Search in Set.
        if cur_node not in visitied:
            visitied.add(cur_node)
            ret.append((cur_node, cur_accumulative_sum))

            for next in adj_list[cur_node][1:]:
                next_node, next_edge = next
                search_stack.append((next_node, next_edge + cur_accumulative_sum))

    return max(ret, key=lambda x:x[1])

# Conduct DFS two times.
def sol(adj_list):
    root = 1
    leaf_node, _ = dfs(root, adj_list)
    _, dist_from_leaf = dfs(leaf_node, adj_list)
    return dist_from_leaf

print(sol(get_input()))