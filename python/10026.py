from collections import deque

n = int(input())

img = []
img_weak = []
for _ in range(n):
    img.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(img, search_color_list):
    search_stack = deque([])
    visited = set([])
    block_cnt = 0

    for i in range(n):
        for j in range(n):
            if img[i][j] in search_color_list:
                search_stack.append((i, j, True))

    while search_stack:
        x, y, is_init = search_stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if is_init:
            block_cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # Check is there any block that could visit later.
            if (nx, ny) not in visited and img[nx][ny] in search_color_list:
                search_stack.append((nx, ny, False))
    return block_cnt

b_count = bfs(img, ['B'])
print(bfs(img, ['R']) + bfs(img, ['G']) + b_count)
print(bfs(img, ['R', 'G']) + b_count)