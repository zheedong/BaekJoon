import sys
sys.setrecursionlimit(int(1e9))

T = int(input())

def dfs(node):
    global selected_students, visited, finished, cnt
    visited[node] = True
    next = selected_students[node]
    if not visited[next]:
        dfs(next)
    elif not finished[next]:
        temp = next
        while True:
            cnt += 1
            temp = selected_students[temp]
            if temp == next:
                break
    finished[node] = True

for _ in range(T):
    n = int(input())
    selected_students = list(map(lambda x: x-1, map(int, input().split())))

    visited = [False for _ in range(n)]
    finished = [False for _ in range(n)]
    cnt = 0

    for node in range(n):
        if not visited[node]:
            dfs(node)
    print(n - cnt)