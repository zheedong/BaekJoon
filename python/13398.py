n = int(input())
accum_sum = list(map(int, input().split()))
accum_sum = [0] + accum_sum
for i in range(1, n + 1):
    accum_sum[i] += accum_sum[i - 1]
print(accum_sum)