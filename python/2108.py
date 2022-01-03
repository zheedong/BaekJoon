import sys
from collections import Counter

n = int(input())

inp_list = []

for _ in range(n):
    inp_list.append(int(sys.stdin.readline().strip()))
    
inp_list.sort()

mean = round(sum(inp_list) / n)
mid = inp_list[int(n / 2)]

count_list = (sorted(Counter(inp_list).most_common(), key = lambda x : -x[1]))
if len(count_list) == 1:
    common = count_list[0][0]
elif count_list[0][1] != count_list[1][1]:
    common = count_list[0][0]
else:
    common = count_list[1][0]

my_range = inp_list[-1] - inp_list[0]

print(mean)
print(mid)
print(common)
print(my_range)