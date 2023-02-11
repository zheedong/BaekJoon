n, m = map(int, input().split())
paint = []

for row in range(n):
    paint.append(list(str(input())))
    for col in range(m // 2):
        if paint[row][col] == '.' and paint[row][m - 1 - col] != '.':
            paint[row][col] = paint[row][m - 1 - col]
        elif paint[row][col] != '.' and paint[row][m - 1 - col] == '.':
            paint[row][m - 1 - col] = paint[row][col]

for row in paint:
    print(''.join(row))
