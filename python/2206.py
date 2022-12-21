import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int ,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0] * m for _ in range(n)] for _ in range(2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(crush, _x, _y):
    queue = deque()
    queue.append([crush, _x, _y])
    visited[crush][_x][_y] = 1

    while queue:
        crush, x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[crush][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[crush][nx][ny] == 0:
                if graph[nx][ny] == 1 and crush == 0:
                    queue.append([1, nx, ny])
                    visited[1][nx][ny] = visited[crush][x][y] + 1
                if graph[nx][ny] == 0:
                    queue.append([crush, nx, ny])
                    visited[crush][nx][ny] = visited[crush][x][y] + 1
    return -1

print(bfs(0, 0, 0))