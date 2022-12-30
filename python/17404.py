import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

R, G, B = 0, 1, 2

n = int(input().rstrip())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

dp = dict([])

def sol(cur_house_front, prev_front_color, prev_back_color):
    cur_house_back = (n - 1) - cur_house_front
    if cur_house_back < cur_house_front:
        return 0
    elif cur_house_front == cur_house_back:
        ret = int(1e9)
        for cur_color in [R, G, B]:
            if cur_color == prev_front_color or cur_color == prev_back_color:
                continue
            ret = min(ret, cost[cur_house_front][cur_color])
        return ret
    else:
        ret = int(1e9)
        for cur_front_color in [R, G, B]:
            for cur_back_color in [R, G, B]:
                if cur_house_front + 1 == cur_house_back and cur_front_color == cur_back_color:
                    continue
                if cur_front_color == prev_front_color or cur_back_color == prev_back_color:
                    continue
                try:
                    ret = min(ret, dp[(cur_house_front, cur_front_color, cur_back_color)])
                except:
                    dp[(cur_house_front, cur_front_color, cur_back_color)] = \
                    cost[cur_house_front][cur_front_color] + cost[cur_house_back][cur_back_color] + sol(cur_house_front + 1, cur_front_color, cur_back_color)
                    ret = min(ret, dp[(cur_house_front, cur_front_color, cur_back_color)])
        return ret


min_val = int(1e9)
for init_color in [R, G, B]:
    for last_color in [R, G, B]:
        if init_color == last_color:
            continue
        min_val = min(min_val, cost[0][init_color] + cost[n - 1][last_color] + sol(1, init_color, last_color))
print(min_val)
