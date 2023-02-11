import sys
from collections import deque
input = sys.stdin.readline

h, w, l = map(int, input().split())
word_grid = []
for _ in range(h):
    word_grid.append(list(str(input())))
target_word = list(str(input()))

total_cnt = 0

nx = [-1, 0, 1, -1, 1, -1, 0, 1]
ny = [-1, -1, -1, 0, 0, 1, 1, 1]

dp = dict([])

def sol(i, j, idx):
    if (i, j, idx) in dp.keys():
        return dp[(i, j, idx)]
    elif idx == l - 1:
        return 1
    else:
        cnt = 0
        for n in range(8):
            next_i = i + nx[n]
            next_j = j + ny[n]
            if 0 <= next_i < h and 0 <= next_j < w and word_grid[next_i][next_j] == target_word[idx + 1]:
                cnt += sol(next_i, next_j, idx + 1)
        dp[(i, j, idx)] = cnt
        return cnt

for i, row in enumerate(word_grid):
    for j, col in enumerate(row):
        if word_grid[i][j] == target_word[0]:
            total_cnt += sol(i, j, 0)

print(total_cnt)
