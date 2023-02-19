n, m = map(int, input().split())

adj_mat = [[None] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj_mat[u].append(v)
    adj_mat[v].append(u)

k = int(input())
destroyed_city = set(map(int, input().split()))

bomb_city = set([])
cur_map = set([])

for city, near_city in enumerate(adj_mat):
    if city == 0:
        continue
    near_city = set(near_city[1:])
    near_city.add(city)
    if near_city - destroyed_city == set([]):
        bomb_city.add(city)
        cur_map = cur_map.union(near_city)

if cur_map == destroyed_city:
    print(len(bomb_city))
    print(*bomb_city)
else:
    print(-1)

