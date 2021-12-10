import sys
sys.setrecursionlimit(1000000)

count_dict = dict([])

count_dict[1] = 1
count_dict[2] = 1
count_dict[3] = 1

MAX = 987654321987654321987654321

def get_minimum(n):
    ret = 0
    if n in count_dict:
        return count_dict[n]
    elif n % 3 != 0 and n % 2 != 0:
        ret = get_minimum(n-1) + 1
    elif n % 3 == 0 and n % 2 != 0:
        ret = min(get_minimum(int(n / 3)), get_minimum(n - 1)) + 1
    elif n % 3 != 0 and n % 2 == 0:
        ret = min(get_minimum(int(n / 2)), get_minimum(n - 1)) + 1
    else:
        ret =  min(get_minimum(int(n / 3)),
                   get_minimum(int(n / 2)),
                   get_minimum(int(n - 1)),
               ) + 1        
    count_dict[n] = ret
    return ret
    
n = int(input())
        
print(get_minimum(n))
print(len(count_dict))