import heapq

n = int(input())

def get_distance(co1, co2):
    x1, y1 = co1
    x2, y2 = co2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

INF = int(1e5)

edges = []
coordi = []

for _ in range(n):
    coordi.append(tuple(map(float, input().split())))

for row in range(n):
    for col in range(row, n):
        if row == col:
            continue
        dist = get_distance(coordi[row], coordi[col])
        heapq.heappush(edges, (dist, row, col))

visited = [False for _ in range(n)]
sum_dist = 0

def prim(start_node):
    global visited, sum_dist

    visited[start_node] = True
    not_searched = []

    while edges:
        cand_dist, cand_start, cand_end = heapq.heappop(edges)
        if visited[cand_start] and not visited[cand_end]:
            sum_dist += cand_dist
            for x in not_searched:
                heapq.heappush(edges, x)
            prim(cand_end)
            break
        elif not visited[cand_start] and visited[cand_end]: 
            sum_dist += cand_dist
            for x in not_searched:
                heapq.heappush(edges, x)
            prim(cand_start)
            break
        else:
            not_searched.append((cand_dist, cand_start, cand_end))
    else:
        return

prim(0)
print(sum_dist)
