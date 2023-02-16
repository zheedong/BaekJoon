SOUTH = 0
EAST = 1
NORTH = 2
WEST = 3
cur_direction = SOUTH

n = int(input())
movements = list(input())

# x, y
cur_posn = (0, 0)

poss_posn = {(0, 0)}

for mov in movements:
    if mov == 'R':
        cur_direction = (cur_direction + 3) % 4
    if mov == 'L':
        cur_direction = (cur_direction + 1) % 4
    if mov == 'F':
        if cur_direction == WEST:
            cur_posn = (cur_posn[0] - 1, cur_posn[1])
        elif cur_direction == EAST:
            cur_posn = (cur_posn[0] + 1, cur_posn[1])
        elif cur_direction == NORTH:
            cur_posn = (cur_posn[0], cur_posn[1] + 1)
        elif cur_direction == SOUTH:
            cur_posn= (cur_posn[0], cur_posn[1] - 1)
        poss_posn.add(cur_posn)

poss_posn = list(poss_posn)
min_x = min(0, min(list(map(lambda x: x[0], poss_posn))))
min_y = min(0, min(list(map(lambda x: x[1], poss_posn))))
poss_posn = list(map(lambda x: (x[0] - min_x, x[1] - min_y), poss_posn))

max_x = max(list(map(lambda x: x[0], poss_posn)))
max_y = max(list(map(lambda x: x[1], poss_posn)))

maze = [['#' for _ in range(max_y + 1)] for _ in range(max_x + 1)]

for cur_posn in poss_posn:
    x, y = cur_posn
    maze[max_y - y][x] = '.'

for row in maze:
    print("".join(row))

