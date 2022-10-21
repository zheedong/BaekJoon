import sys
input = sys.stdin.readline

n, k = map(int, input().split())

weight_lst = []
value_lst = []
for _ in range(n):
    w, v = map(int, input().split())
    weight_lst.append(w)
    value_lst.append(v)

# 0-1 knapsack probelm
# https://comdoc.tistory.com/entry/35-배낭문제Knapsack-problem-파이썬

# naive-recursion. 당연히 시간 초과.
# 전체적인 모습 보기 위해 만듦.
def bag_sol(capacity, n):
    # 더이상 가방에 여유 공간이 없거나, 넣을 수 있는 물건이 없을 때.
    if capacity == 0 or n == 0:
        return 0
    else:
        # n은 이전에 고른 물건의 index의 의미. 처음 시작을 총 갯수로 시작.
        # n이 정확히 뭔지 좀 애매하다고 생각했는데... 그냥 recursion에서 index를 의미하는 숫자인 듯?
        cur_weight = weight_lst[n - 1]
        cur_val = value_lst[n - 1]
        # 지금 물건의 무게가 가방에 넣을 수 없을 때 
        if cur_weight > capacity:
            # 이번 물건은 건너 뛴다
            return bag_sol(capacity, n - 1)
        # 지금 물건을 가방에 넣을 수 있을 떄
        else:
            # 지금 가치 + capacity가 감소한 가방에서 최대의 가치 vs 이번은 건너뛰었을 때 최대 가치
            return max(cur_val + bag_sol(capacity - cur_weight, n - 1), bag_sol(capacity, n - 1))

# capacity, n을 받아서 value
# dictionary로 처음 시도해 봤는데 역시나 메모리 초과. 음~
# list로 했는데도 PyPy는 메모리 초과 됨. 1%를 못 넘어감...
# sys.setrecursionlimit(10 ** 8) 로 처음 했었는데 지우니까 PyPy로도 된다. 햐 파이썬 진짜...
dp_list = [[None] * (n + 1) for _ in range(k + 1)]

# DP 적용에서 특별한 건 없다. [capacity][n] 에 값을 저장해 놓기.
def dp_bag_sol(capacity, n):
    # 이미 알고 있다면 return
    if dp_list[capacity][n] != None:
        return dp_list[capacity][n]
    else:
        if capacity == 0 or n == 0:
            return 0
        else:
            cur_weight = weight_lst[n - 1]
            cur_val = value_lst[n - 1]
            if cur_weight > capacity:
                # 계산된 값을 저장.
                dp_list[capacity][n] = dp_bag_sol(capacity, n - 1)
            else:
                # 계산된 값을 저장 2
                dp_list[capacity - cur_weight][n - 1] = dp_bag_sol(capacity - cur_weight, n - 1)
                dp_list[capacity][n - 1] = dp_bag_sol(capacity, n - 1)

                # dp_list에서 값들을 가져와서 비교.
                dp_list[capacity][n] = max(cur_val + dp_list[capacity - cur_weight][n - 1], dp_list[capacity][n - 1])
            # 최종적인 결과를 return.
            return dp_list[capacity][n]

# print(bag_sol(k, n))
print(dp_bag_sol(k, n))