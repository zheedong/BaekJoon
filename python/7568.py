n = int(input())

inp_list = []

for _ in range(n):
    x, y = map(int, input().split())
    inp_list.append((x,y))
    
res_list = [1 for i in range(n)]

for i in range(len(inp_list)):
    cur_size = inp_list[i]
    for size in inp_list:
        cur_x, cur_y = cur_size
        x, y = size
        if cur_x < x and cur_y < y:
            res_list[i] += 1

for x in res_list:
    print(x, end = " ")