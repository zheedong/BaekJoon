n = int(input())

adj_list = []

for i in range(n):
    adj_list.append(list(map(int, input().split())))

print(adj_list)