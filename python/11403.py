import sys
input = sys.stdin.readline

INF = 9999999999
n = int(input().rstrip())

adj_mat = [[None] * (n + 1) for _ in range(n + 1)]
# 혼동을 피하기 위해 사용하지 않는 0열, 0행은 None
for row in adj_mat[1:]:
    row[1:] = list(map(lambda x : INF if x == 0 else 1, list(map(int, input().split()))))

# 플로이드-워셜 알고리즘
# 시간 복잡도 O(V^3), 모든 노드에서 모든 노드의 거리를 구하는 상황.
for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if adj_mat[start][end] > adj_mat[start][mid] + adj_mat[mid][end]:
                adj_mat[start][end] = adj_mat[start][mid] + adj_mat[mid][end]

for row in adj_mat[1:]:
    print(*list(map(lambda x : 0 if x == INF else 1,row[1:])))