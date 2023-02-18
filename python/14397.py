n, m = map(int, input().split())

beach_map = []

for _ in range(n):
    beach_map.append(list(input()))

near_i = [-1, -1, 0, 0, 1, 1]
near_j = [0, 1, -1, 1, 0, 1]

near_i_even = [-1, -1, 0, 0, 1, 1]
near_j_even = [-1, 0, -1, 1, -1, 0]

cnt = 0

for i in range(n):
    for j in range(m):
        if beach_map[i][j] == '#':
            for near in range(6):
                if i % 2 == 1:
                    if 0 <= i + near_i[near] < n and 0 <= j + near_j[near] < m and beach_map[i + near_i[near]][j + near_j[near]] == '.':
                        cnt += 1
                else:
                    if 0 <= i + near_i_even[near] < n and 0 <= j + near_j_even[near] < m and beach_map[i + near_i_even[near]][j + near_j_even[near]] == '.':
                        cnt += 1


print(cnt)



'''
i j => i-1 j / i-1 j+1 / i j-1 / i j+1 / i+1 j / i+1 j+1
i j => i-1 j-1 / i-1 j / i j-1 / i j+1 / i+1 j-1 / i+1 j
'''
