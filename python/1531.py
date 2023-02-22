n, m = map(int, input().split())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    left_x, left_y, right_x, right_y = map(lambda x: x-1, map(int, input().split()))
    for row in range(left_x, right_x + 1):
        for col in range(left_y, right_y + 1):
            paper[row][col] += 1

ans = 0

for row in paper:
    for pic in row:
        if pic > m:
            ans += 1

print(ans)
         
