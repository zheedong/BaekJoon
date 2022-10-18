# dijkstra algorithm
import sys
input = sys.stdin.readline

# 상수 정의
INF_COST = 10 ** 10

# 도시의 수
n = int(input())
# 버스의 수
m = int(input())

dist = [[INF_COST]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    bus_from, bus_to, bus_cost = map(int, input().split())
    # 질문 보고 알았음 - A에서 B까지 가는 버스가 여러대 일 수도 있다. 그래서 둘 중 작은 값을 저장한다.
    dist[bus_from][bus_to] = min(dist[bus_from][bus_to], bus_cost)

min_cost_start, min_cost_end = map(int, input().split())

'''
# Test Case
n = 5
m = 8
dist = [[INF_COST]*(n + 1) for _ in range(n + 1)]
dist[1][2] = 2
dist[1][3] = 3
dist[1][4] = 1
dist[1][5] = 10
dist[2][4] = 2
dist[3][4] = 1
dist[3][5] = 1
dist[4][5] = 3
min_cost_start, min_cost_end = 1, 5
# TC End
'''

# 혼동을 피하기 위해 index = 0 은 사용하지 않으니 None으로 처리
dist[0] = [None] * (n + 1)
for row in dist:
    row[0] = None

def get_nearest(shortest_dist, nodes):
    nearest_node = None
    nearest_cost = INF_COST
    for node in nodes:
        # 최단 노드를 구하는 연산을 반복한다
        if nearest_cost > shortest_dist[node]:
            nearest_node = node
            nearest_cost = shortest_dist[node]
    return nearest_node

def get_not_visited(is_visited):
    ret = []
    for idx, node in enumerate(is_visited):
        if node == False:
            ret.append(idx)
    return ret

# list 말고 우선순위 큐로 구현하면 더 빠르다고 하다.
def get_nearest_not_visited_node(shortest_dist, is_visited):
    return get_nearest(shortest_dist, get_not_visited(is_visited))

# 방문할 수 있는 모든 node를 구한다. 0과 현재 노드를 제외.
def get_can_go_nodes(cur_node):
    ret = [i for i in range(1, n + 1)]
    ret.remove(cur_node)
    return ret

# 방문 저장용 list
is_visited = [False] * (n + 1)
# 혼동을 피하기 위해 배열의 0은 사용하지 않는다.
is_visited[0] = None

# 나무위키 참고 했다.

# 1 - 출발점으로부터 최단 거리를 저장하는 list.
shortest_dist = [INF_COST for _ in range(n + 1)]
# 혼동을 피하기 위해 배열의 0은 사용하지 않는다.
shortest_dist[0] = None
# 출발 지점은 0, 나머지는 INF로 설정한다. 
shortest_dist[min_cost_start] = 0

# 2 - 현재 노드를 나타내는 변수 A. 시작 지점으로 초기화 한다.
current_node = min_cost_start

while(True):
    # 8 - 목표 지점을 방문 했거나, 더이상 방문할 수 있는 노드가 없으면 종료한다.
    if is_visited[min_cost_end] or current_node == None:
        break

    # 3 4 5 - 현재 노드에서 갈 수 있는 모든 노드에 대해 다음을 실행한다.
    for can_go_node in get_can_go_nodes(current_node):
        # d[A] + P[A][B] 와 d[B] 를 비교해 최단거리를 업데이트 한다.
        shortest_dist[can_go_node] = min(shortest_dist[can_go_node], shortest_dist[current_node] + dist[current_node][can_go_node])
    # 6 - 갈 수 있는 모든 노드를 방문했으면 표시한다.
    is_visited[current_node] = True

    # 7 - 방문하지 않은 노드 중에서 가장 가까운 노드를 구한다.
    current_node = get_nearest_not_visited_node(shortest_dist, is_visited)
print(shortest_dist[min_cost_end])