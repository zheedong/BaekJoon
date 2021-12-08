n = int(input())

coordinate_list = []

for i in range(0, n):
    x_i, y_i = map(int, input().split())
    coordinate_list.append((x_i, y_i))
    
coordinate_list.sort()

for i in range(0, n):
    x_i, y_i = map(str, coordinate_list[i])
    print(x_i + " " + y_i)