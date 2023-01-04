from collections import deque

r, c = map(int, input().split())
inp = []
alphabet = set([])
for i in range(r):
    inp.append(list(input()))
    for x in inp[i]:
        alphabet.add(x)

def alphabet_to_int(char):
    return ord(char) - ord('A')


search_stack = deque([(0, 0, 1)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_depth = -1
visited = [False for _ in range(26)] 
visited[alphabet_to_int(inp[0][0])] = True

def dfs(x, y, cur_depth):
    global max_depth
    max_depth = max(max_depth, cur_depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[alphabet_to_int(inp[nx][ny])]:
                visited[alphabet_to_int(inp[nx][ny])] = True
                dfs(nx, ny, cur_depth + 1)
                visited[alphabet_to_int(inp[nx][ny])] = False


dfs(0, 0, 1)
print(max_depth)
