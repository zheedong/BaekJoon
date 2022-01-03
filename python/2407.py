n, m = map(int, input().split())

comb_dict = dict([])
comb_dict[(0, 0)] = 1
comb_dict[(1, 0)] = 1
comb_dict[(1, 1)] = 1

def get_comb(inp):
    n, m = inp
    if m == 0:
        return 1
    elif n == m:
        return 1
    else:
        try:
            return comb_dict[inp]
        except:
            ret = get_comb((n-1, m-1)) + get_comb((n-1, m))
            comb_dict[inp] = ret
            return ret
        
print(get_comb((n, m)))