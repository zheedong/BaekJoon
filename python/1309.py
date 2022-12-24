from collections import deque

n, m = map(int, input().split())

blue = []
white = []

for row in range(m):
    inp = list(input())
    for col, color in enumerate(inp):
        if color == 'B':
            blue.append((row, col))
        else:
            white.append((row, col))

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
        
def dfs(color_list):
    visited = set([])
    ret = []
    for init in color_list:
        search_stack = deque([init])
        block_cnt = 0
        while search_stack:
            cur_x, cur_y = search_stack.pop()
            if (cur_x, cur_y) in visited:
                continue
            visited.add((cur_x, cur_y))
            block_cnt += 1
            for i in range(4):
                next_x, next_y = cur_x + nx[i], cur_y + ny[i]
                if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
                    continue
                if (next_x, next_y) in color_list:
                    search_stack.append((next_x, next_y))
        ret.append(block_cnt)
    return ret

print(sum(map(lambda x : x ** 2, dfs(white))), sum(map(lambda x : x ** 2, dfs(blue))))