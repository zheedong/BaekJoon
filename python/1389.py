import sys
input = sys.stdin.readline

INF = 9999999999
n, m = map(int, input().split())

friend_mat = [[INF] * (n + 1) for _ in range(n + 1)]
# 혼동을 피하기 위해 사용하지 않는 0열, 0행은 None
friend_mat[0] = [None] * (n + 1)
for row in friend_mat:
    row[0] = None

for _ in range(m):
    fri_1, fri_2, = map(int, input().split())
    friend_mat[fri_1][fri_2] = 1
    friend_mat[fri_2][fri_1] = 1

# 플로이드-워셜 알고리즘
# 시간 복잡도 O(V^3), 모든 노드에서 모든 노드의 거리를 구하는 상황.
for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if friend_mat[start][end] > friend_mat[start][mid] + friend_mat[mid][end]:
                friend_mat[start][end] = friend_mat[start][mid] + friend_mat[mid][end]
    
ret = []
for row in friend_mat[1:]:
    ret.append(sum(row[1:]))
# argmin이 없어서 직접 구현...
print(min(range(len(ret)), key=lambda i : ret[i]) + 1)