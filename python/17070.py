from collections import deque

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

def get_pipe_end(pipe):
    x, y, state = pipe
    if state == 0:
        return x, y + 1
    elif state == 1:
        return x + 1, y
    else:
        return x + 1, y + 1

def get_next(pipe):
    _, _, state = pipe
    nx, ny = get_pipe_end(pipe)
    if state == 0:
        return [(nx, ny, 0), (nx, ny, 1)]
    elif state == 1:
        return [(nx, ny, 1), (nx, ny, 2)]
    else:
        return [(nx, ny, 0), (nx, ny, 1), (nx, ny, 2)]

def is_possilbe(pipe):
    x, y, state = pipe

pipe_state = 0
cnt = 0

# 가로, 세로, 대각선 : 0, 1, 2
search_queue = deque([(0, 0, 0)])
while search_queue:
    cur_pipe = search_queue.popleft()
    x, y, _ = cur_pipe
    end_x, end_y = get_pipe_end(cur_pipe)
    if house[x][y] == 1 or house[end_x][end_y] == 1:
        continue
    elif end_x == end_y == (n - 1):
        cnt += 1
    else:
        for next_pipe in get_next(cur_pipe):
            nendx, nendy = get_pipe_end(next_pipe)
            if nendx >= n or nendy >= n:
                continue
            search_queue.append(next_pipe)
    
print(cnt)