# Fucking Union-Find. Can not understand!!
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]
planes = [int(input().rstrip()) for _ in range(P)]
answer = 0

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

for plane in planes:
    docking = find(plane)
    if docking == 0:
        break
    else:
        parent[docking] = parent[docking - 1]
        answer += 1

print(answer)