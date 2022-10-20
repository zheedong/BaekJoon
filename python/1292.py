a, b = map(int, input().split())

math_lst = [1]
num = 2

while(len(math_lst) < b):
    for _ in range(num):
        math_lst.append(num)
    num += 1

print(sum(math_lst[a - 1:b]))