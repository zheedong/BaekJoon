n, m = map(int, input().split())
k = int(input())
on_working = set()
for _ in range(k):
    a, b, c, d = map(int, input().split())
    if a + b > c + d:
        on_working.add((c, d, a, b))
    else:
        on_working.add((a, b, c, d))

nx = [1, 0]
ny = [0, 1]

cnt = 0
dp = dict([])

def sol(cur_x, cur_y):

    if (cur_x, cur_y) in dp.keys():
        return dp[(cur_x, cur_y)]

    if cur_x == n and cur_y == m:
        return 1
        
    cnt = 0
    for i in range(2):
        next_x = cur_x + nx[i]
        next_y = cur_y + ny[i]
        if 0 <= next_x <= n and 0 <= next_y <= m and (cur_x, cur_y, next_x, next_y) not in on_working:
            cnt += sol(next_x, next_y)
    dp[(cur_x, cur_y)] = cnt
    return cnt
            
print(sol(0, 0))
