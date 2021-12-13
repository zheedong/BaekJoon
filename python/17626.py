# 일단 포기

import math

n = int(input())

min_square_dict = dict([])
min_square_dict[1] = 1    # 1^2

def get_min_square(n):
    gaus_sqrt_n = int(math.sqrt(n))
    
    if math.pow(gaus_sqrt_n, 2) == n:
        min_square_dict[n] = 1
        return
    
    min_square_dict[n] = n    # 1^2 + ... n번
    for i in range(2, n):
        if min_square_dict[n] > 
        
get_min_square(n)
print(min_square_dict[n])