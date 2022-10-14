import sys
input = sys.stdin.readline

n = int(input())

connected_node = dict([])
node_parent = dict([])

for i in range(1, n + 1):
    connected_node[i] = []
    node_parent[i] = []

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    connected_node[node1].append(node2)
    connected_node[node2].append(node1)

def solution(parent_node):
    try:
        for child_node in connected_node[parent_node]:
            node_parent[child_node] = parent_node
            connected_node[child_node].remove(parent_node)
            solution(child_node)
        return
    except:
        return

solution(1)
for node in list(node_parent.values())[1:]:
    print(node)