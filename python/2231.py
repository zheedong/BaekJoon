n = input()

def get_div_sum(n):
    n = str(n)
    ret = 0
    for k in n:
        ret += int(k)
    return ret + int(n)

ret = 0

for i in range(int(n)):
    if get_div_sum(i) == int(n):
        ret = i
        break
        
print(ret)