import sys
input = sys.stdin.readline

n = int(input().rstrip()) 
m = int(input().rstrip())

INF = 9999999999999

min_dist = [[None for _ in range(n + 1)]]
min_dist += [[INF for _ in range(n + 1)] for _ in range(n)]
for idx, _ in enumerate(min_dist):
    min_dist[idx][0] = None

for _ in range(m):
    a, b, c = map(int, input().split())
    min_dist[a][b] = min(min_dist[a][b], c)

# Easy Floyd Warshall algorithm
# n is small, so you don't need to worry about O(n^3)
for m in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if s == e:
                continue
            if min_dist[s][e] > min_dist[s][m] + min_dist[m][e]:
                min_dist[s][e] = min_dist[s][m] + min_dist[m][e]

for row in min_dist[1:]:
    print(*list(map(lambda x : 0 if x >= INF else x ,row[1:])))