n, m = map(int, input().split())

gorani_dist = []

for _ in range(n):
    gorani_dist.append(list(map(int, input().split())))

min_r_dist = int(1e9)
min_c_dist = int(1e9)
min_r = None
min_c = None

for idx, row in enumerate(gorani_dist):
    if min_r_dist > row[0]:
        min_r_dist = row[0]
        min_r = idx
for idx, col in enumerate(gorani_dist[-1]):
    if min_c_dist > col:
        min_c_dist = col
        min_c = idx

print(min_r + 1, min_c + 1)
