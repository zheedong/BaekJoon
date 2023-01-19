# Board Game Cup B

n = int(input())
s = 0
b = 0
l = 0
p = 0

for _ in range(n):
    fruit, fru_num = input().split()
    fru_num = int(fru_num)
    if fruit == "STRAWBERRY":
        s += fru_num
    elif fruit == "BANANA":
        b += fru_num
    elif fruit == "LIME":
        l += fru_num
    elif fruit == "PLUM":
        p += fru_num

for num in [s, b, l, p]:
    if num == 5:
        print("YES")
        break
else:
    print("NO")
