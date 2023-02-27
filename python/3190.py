import sys
from collections import deque
input = sys.stdin.readline

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

n = int(input().rstrip())
game_map = [[0 for _ in range(n)] for _ in range(n)]

k = int(input().rstrip())

apple_posn = []
for _ in range(k):
    row, col = map(int, input().split())
    apple_posn.append((row - 1, col - 1))

move_lst = deque([])
l = int(input().rstrip())
for _ in range(l):
    x, c = map(lambda x: (int(x[0]), x[1]), input().split())
    move_lst.append((x, c))

game_map[0][0] = 1
snake_posn = (0, 0)
snake_dir = EAST
snake_len = 1
cur_time = 0

while True:
    cur_time += 1

