mat = []
max_val = -1
max_idx = None
for i in range(9):
    mat.append(list(map(int, input().split())))
    for j in range(9):
        if mat[i][j] > max_val:
            max_val = mat[i][j]
            max_idx = (i + 1, j + 1)

print(max_val)
print(*max_idx)