n, m = map(int, input().split())
mat1 = []
ret = []
for _ in range(n):
    mat1.append(list(map(int, input().split())))
for row in range(n):
    mat2_row = list(map(int, input().split()))
    ret.append([i + j for i, j in zip(mat1[row], mat2_row)])

for row in ret:
    print(*row)