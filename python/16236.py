from collections import deque

n = int(input())
state = []

class BabyShark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordi = (x, y)
        self.size = 2
        self.eat = 0

    def levelup(self):
        while self.eat >= self.size:
            self.size += 1
            self.eat -= self.size

for _ in range(n):
    state.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if state[i][j] == 9:
            baby_shark = BabyShark(i, j)
            state[i][j] = 0
            break

def get_eatable():
    ret = set([])
    for i in range(n):
        for j in range(n):
            if state[i][j] > 0 and state[i][j] < baby_shark.size:
                ret.add((i, j))
    return ret

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def bfs(time):
    search_queue = deque([(baby_shark.coordi, time)])
    while search_queue:
        cur_pos, cur_time = search_queue.popleft()
        cur_x, cur_y = cur_pos
        if cur_pos in food_list:
            state[cur_x][cur_y] = 0
            baby_shark.x = cur_x
            baby_shark.y = cur_y
            baby_shark.eat += 1
            return cur_time
        for i in range(4):
            next_x = cur_x + nx[i]
            next_y = cur_y + ny[i]
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                continue
            if state[next_x][next_y] < baby_shark.size:
                search_queue.append(((next_x, next_y), cur_time + 1))

time = 0
while True:
    food_list = get_eatable()

    if len(food_list) == 0:
        print(time)
        break

    time = bfs(time)
    baby_shark.levelup()