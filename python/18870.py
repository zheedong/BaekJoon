import sys

n = int(input())

x_list = list(map(int, sys.stdin.readline().split()))
sorted_x = sorted(list(set(x_list)))
x_dict = dict()        # O(n)인 .index() 함수가 아니라 O(1) 인 Hash Table 이용

for i in range(len(sorted_x)):
    x_dict[sorted_x[i]] = i

for x in x_list:
    print(x_dict[x], end = " ")        # O(n^2), 1조번 연산 필요 ^^
print()