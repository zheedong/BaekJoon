# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# Python3만 됨. PyPy X
import sys

n = int(input())
possible_num_list = [0 for i in range(0, 10001)]

for _ in range(0, n):
    possible_num_list[int(sys.stdin.readline().strip())] += 1
    
for num_index in range(0,len(possible_num_list)):
    for i in range(0,possible_num_list[num_index]):
        print(num_index)