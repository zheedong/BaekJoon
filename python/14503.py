NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

n, m = map(int, input().split())
r, c, d = map(int, input().split())

trash_map = []
for _ in range(n):
    trash_map.append(list(map(int, input().split())))

answer = 0

# N E S W order
nr = [-1, 0, 1, 0]
nc = [0, 1, 0, -1]

NOT_CLEAN = 0
WALL = 1
CLEAN = 2

while True:
    # 1. If not cleaned, clean it 
    if trash_map[r][c] == NOT_CLEAN:
        answer += 1
        trash_map[r][c] = CLEAN
        continue

    for _ in range(4):
        d = (d + 3) % 4
        near_r, near_c = r + nr[d], c + nc[d]

        # 3. Yes not cleaned near
        if 0 <= near_r < n and 0 <= near_c < m and trash_map[near_r][near_c] == NOT_CLEAN:
            r = near_r
            c = near_c
            break

    else:
        # 2. No not cleaned near
        back_r, back_c = r + nr[(d + 2) % 4], c + nc[(d + 2) % 4]
        if 0 <= back_r < n and 0 <= back_c < m and trash_map[back_r][back_c] != WALL:
            r = back_r
            c = back_c
            continue
        else:
            break

print(answer)

