from collections import deque
from distutils import dep_util

# Graph / BFS
maze_matrix = []

# Key = tuple, Value = list of tuple
# node 값이 1인 경우, 인접한 node를 저장한다.
maze_graph = dict()

n, m = map(int, input().split())

for row in range(n):
    inp_row = list(map(int, list(input())))
    maze_matrix.append(inp_row)

# 인근 node 중 값이 1인 것을 찾는다.
def get_adj_node(node, max_size):
    row, col = node
    n, m = max_size
    adj_node_list = []
    # matrix 범위를 벗어나지 않게 주의.
    if row - 1 >= 0 and maze_matrix[row - 1][col] == 1:
        adj_node_list.append((row - 1, col))
    if row + 1 <= n - 1 and maze_matrix[row + 1][col] == 1:
        adj_node_list.append((row + 1, col)) 
    if col - 1 >= 0 and maze_matrix[row][col - 1] == 1:
        adj_node_list.append((row, col - 1))
    if col + 1 <= m - 1 and maze_matrix[row][col + 1] == 1:
        adj_node_list.append((row, col + 1))
    return adj_node_list

# node가 방문 되었을 때 depth를 저장한다.
node_depth_dict = dict()
# node를 방문 했었는지 기록한다.
node_searched_bool = dict()

for row in range(n):
    for col in range(m):
        cur_node = (row, col)
        # node가 값이 1인 경우에만 인접 node를 구한다.
        if maze_matrix[row][col] == 1:
            # Depth는 임의의 큰 값이 초기값.
            node_depth_dict[cur_node] = 9999999
            node_searched_bool[cur_node] = False
            maze_graph[cur_node] = get_adj_node(cur_node, (n, m))

bfs_queue = deque([(0, 0)])
node_depth_dict[(0, 0)] = 1

while bfs_queue:
    cur_search_node = bfs_queue.popleft() 
    # 방문 했었다면 패스.
    if node_searched_bool[cur_search_node]:
        continue
    # 방문 표시
    node_searched_bool[cur_search_node] = True
    for node in maze_graph[cur_search_node]:
        bfs_queue.append(node)
        # 새롭게 추가 되는 node의 depth를 결정한다. 현재 값과 새로운 값 사이의 비교를 함에 주의.
        node_depth_dict[node] = min(node_depth_dict[cur_search_node] + 1, node_depth_dict[node])

print(node_depth_dict[(n - 1, m - 1)])