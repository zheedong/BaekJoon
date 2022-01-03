from itertools import product

n, m = map(int, input().split())

inp_list = list(map(int, input().split()))


        
for out in sorted(res):
    for num in out:
        print(num, end = " ")
    print()