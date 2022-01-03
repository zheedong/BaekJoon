# f(n) = f(n-1) + f(n-5)

pado_dict = dict([])

pado_dict[1] = 1
pado_dict[2] = 1
pado_dict[3] = 1
pado_dict[4] = 2
pado_dict[5] = 2

def sol(num):
    try:
        return pado_dict[num]
    except:
        ret = sol(num - 1) + sol(num - 5)
        pado_dict[num] = ret
        return ret
    
t = int(input())

for _ in range(t):
    n = int(input())
    print(sol(n))