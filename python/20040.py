import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = []
for i in range(n):
    parent.append(i)

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[u] = v
    else:
        parent[v] = u

for idx in range(m):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print(idx + 1)
        break
    else:
        union(x, y)
else:
    print(0)