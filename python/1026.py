n = int(input())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())), reverse=True)

sum = 0
for idx in range(n):
    sum += a_list[idx] * b_list[idx]

print(sum)