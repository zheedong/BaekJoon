n = int(input())
a_list = list(map(int, input().split()))
a_count = [0 for _ in range(n + 1)]
a_count[0] = None
for num in a_list:
    a_count[num] += 1
ret = 1
for num in a_count[1:]:
    ret *= (num + 1)
ret -= 1
print(ret % (10**9 + 7))
