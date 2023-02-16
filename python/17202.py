phone_num_a = list(map(int, list(input())))
phone_num_b = list(map(int, list(input())))

def sol(lst):
    if len(lst) == 2:
        return lst
    else:
        ret = []
        for i in range(len(lst) - 1):
            ret.append((lst[i] + lst[i + 1]) % 10)
        return sol(ret)

inp = []
for x in range(8):
    inp.append(phone_num_a[x])
    inp.append(phone_num_b[x])

output = sol(inp)
print(f"{output[0]}{output[1]}")
