import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

tetris=[[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(0,1),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,1),(1,2),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,1),(1,0),(2,1)]]

max_sum = -1

for i in range(n):
    for j in range(m):
        for shape in tetris:
            tetris_coordis = list(map(lambda x : (x[0] + i, x[1] + j), shape))
            for coordi in tetris_coordis:
                # Check is it in proper range.
                if coordi[0] < 0 or coordi[1] < 0 or coordi[0] >= n or coordi[1] >= m:
                    break
            else:
                max_sum = max(max_sum, sum(list(map(lambda x : table[x[0]][x[1]], tetris_coordis))))

print(max_sum)
