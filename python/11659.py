n, m = map(int, input().split())

inp_list = list(map(int, input().split()))
# 누적 합 알고리즘
prefix_sum = [0]
for i in range(1, len(inp_list)+1):
    prefix_sum.append(prefix_sum[i-1] + inp_list[i-1])

ret_list = []

for _ in range(m):
    i, j = map(int, input().split())
    ret_list.append(prefix_sum[j] - prefix_sum[i-1])
    
for ret in ret_list:
    print(ret)