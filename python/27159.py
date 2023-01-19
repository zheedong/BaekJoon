# Board Game Cup A
n = int(input())
inp = list(map(int, input().split()))

cur_num = inp[0]
res = cur_num
for next_num in inp[1:]:
    if next_num != cur_num + 1:
        res += next_num
    cur_num = next_num

print(res)
