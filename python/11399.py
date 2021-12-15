n = int(input())

p_list = sorted(list(map(int, input().split())))

ret = 0

for i in range(n):
    ret += (n-i) * p_list[i]
    
print(ret)