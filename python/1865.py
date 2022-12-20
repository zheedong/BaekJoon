import sys
input = sys.stdin.readline
INF = int(1e9)

def get_inp():
    edges = []
    n, m, w = map(int, input().split())

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    return n, edges

# https://www.acmicpc.net/board/view/72995
# https://velog.io/@kimdukbae/알고리즘-벨만-포드-알고리즘-Bellman-Ford-Algorithm

def bellmanford(vertex_num, edge_num, edges):
    distance = [0] * (vertex_num + 1)
    # distance[start] = 0
    for i in range(vertex_num):
        for j in range(edge_num):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == vertex_num - 1:
                    return True
    return False

def sol(vertex_num, edges):
    edge_num = len(edges)
    if bellmanford(vertex_num, edge_num, edges):
        return "YES"
    else:
        return "NO"

tc = int(input().rstrip())
for _ in range(tc):
    print(sol(*get_inp()))