from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

apart_list = []
apart_exist_idx = []

for _ in range(n):
    apart_list.append(list(map(int, list(input().rstrip()))))

'''
tc1_n = 7
n = tc1_n
tc1 = [[0, 1, 1, 0, 1, 0, 0],
       [0, 1, 1, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 0, 1, 1, 1],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 0, 0, 0]]
apart_list = tc1
'''

for i, row in enumerate(apart_list):
    for j, col in enumerate(row):
        if apart_list[i][j] == 1:
            apart_exist_idx.append((i, j))

def get_adj_idx(idx, n):
    x, y = idx
    ret = []
    if x != 0:
        ret.append((x - 1, y))
    if y != 0:
        ret.append((x, y - 1))
    if x != n - 1:
        ret.append((x + 1, y))
    if y != n - 1:
        ret.append((x, y + 1))
    return ret

def get_only_apart(adj_apart_list):
    ret = []
    for apart in adj_apart_list:
        x, y = apart
        if apart_list[x][y] == 1:
            ret.append(apart)
    return ret

searched_bool = [[False] * n for _ in range(n)]
ret = []

# 모든 node가 root가 될 수 있다.
for cur_root in apart_exist_idx:
    x_root, y_root = cur_root
    # 이미 방문한 node라면 continue
    if searched_bool[x_root][y_root]:
        continue
    else:
        search_queue = deque([cur_root])
        cur_cnt = 0
        # BFS
        while search_queue:
            cur_apart = search_queue.popleft()
            x, y = cur_apart
            # 방문 여부를 확인
            if searched_bool[x][y] == True:
                continue
            # 아니라면 방문 기록
            else:
                searched_bool[x][y] = True
            next_apart_list = get_only_apart(get_adj_idx(cur_apart, n))
            # 이 덩어리가 방문한 node 수를 저장
            cur_cnt += 1
            # list를 deque에 넣을 땐 extend!
            search_queue.extend(next_apart_list)
        ret.append(cur_cnt)

# 문제 조건이 오름차순 정렬해서 출력
ret.sort()
print(len(ret))
for val in ret:
    print(val)