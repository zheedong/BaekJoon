n = int(input())
res = 1
for i in range(1, n):
    res += n / i
print(res)