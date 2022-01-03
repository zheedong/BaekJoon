t = int(input())

apart_dict = dict([]) 

def get_sol(n):
    x, y = n
    if x == 0:
        return y
    else:
        try:
            return apart_dict[n]
        except:
            res = 0
            for num in range(1, y + 1):
                res += get_sol((x-1, num))
            apart_dict[(x,y)] = res
            return res

for _ in range(t):
    k = int(input())
    n = int(input())
    print(get_sol((k, n)))