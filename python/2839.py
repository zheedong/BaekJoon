n = int(input())

num_of_5 = n // 5

flag = False

for i in range(num_of_5, -1, -1):
    num_of_3 = (n - 5 * i) / 3
    if round(num_of_3) == num_of_3:
        flag = True
        break
        
if flag:
    print(int(num_of_3 + i))
else:
    print(-1)