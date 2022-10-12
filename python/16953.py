from collections import deque

a, b = map(int, input().split())

def node_expand(n):
    return [2*n, 10*n+1]

# None은 Tree의 Depth를 의미한다.
bfs_queue = deque([a, None])
depth = 1

while(True):
    # BFS queue에 None만 있는 경우, 불가능한 경우만 있을 때 (오직 b 보다 작은 값만 queue에 들어가기 때문에)
    if bfs_queue == deque([None]):
        depth = -1
        break

    cur_node = bfs_queue.popleft()

    # 우리가 찾는 경우
    if cur_node == b:
        break
    # Tree depth를 증가시켜야 하는 경우. 앞에서 꺼내서 뒤에 넣어준다.
    elif cur_node == None:
        bfs_queue.append(None)
        depth += 1
    else:
        for node in node_expand(cur_node):
            # b 보다 작은 경우에만 queue 안에 넣어준다.
            if node <= b:
                bfs_queue.append(node)

print(depth)