n = int(input())

house_rgb_cost = dict([])

for house_idx in range(n):
    house_rgb_cost[house_idx] = list(map(int, input().split()))

# 상수
R = 0
G = 1
B = 2
INF_COST = 9999999999

# Naive - recursion
# 느림. 사용되지 않음.
def naive_rec(prev_color, house_idx):
    min_cost = 99999999
    for cur_color in [R, G, B]:
        if cur_color != prev_color:
            min_cost = min(min_cost, house_rgb_cost[house_idx][cur_color] + (0 if house_idx == n -1 else naive_rec(cur_color, house_idx + 1)))
    return min_cost

# Dynamic solution

# house 번호를 받으면 R, G, B를 선택했을 때 비용이 담긴 list
house_cost = dict([])

def dp_solution(prev_color, house_idx):
    try:
        # 이미 DP를 계산했던 경우
        cur_house_rgb_cost = house_cost[house_idx]
        min_cost = INF_COST
        for cur_color in [R, G, B]:
            # 이전 색과 겹치지 않는 경우 중, 가장 작은 cost를 구한다.
            if cur_color != prev_color:
                min_cost = min(min_cost, cur_house_rgb_cost[cur_color])
        return min_cost
    except:
        house_cost[house_idx] = []
        min_cost = INF_COST
        for cur_color in [R, G, B]:
            # 마지막 경우인 경우를 제외하고 재귀적으로 호출한다.
            cur_cost = house_rgb_cost[house_idx][cur_color] + (0 if house_idx == n -1 else dp_solution(cur_color, house_idx + 1))
            # DP에 저장할 값을 업데이트.
            house_cost[house_idx].append(cur_cost)
            if cur_color != prev_color:
                min_cost = min(min_cost, cur_cost)
        return min_cost

print(min(dp_solution(R, 0), dp_solution(G, 0), dp_solution(B, 0)))