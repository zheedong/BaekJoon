import sys

n = int(input())

ordi_list = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    ordi_list.append((x, y))
    
ordi_list.sort(key = lambda x : (x[1], x[0]))    
    
for ordi in ordi_list:
    x, y = ordi
    print(x, y)