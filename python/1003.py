fib_dict = {0:(1,0), 1:(0,1)}
# n : (0, 1)
# Dynamic Programming!

n = int(input())

def add_two_tup(tup1, tup2):
    a, b = tup1
    c, d = tup2
    return (a+c, b+d)

def get_fib_count(k):
    if k in fib_dict:
        return fib_dict[k]
    else:
        add_tup_result = add_two_tup(get_fib_count(k-2), get_fib_count(k-1))
        fib_dict[k] = add_tup_result
        return add_tup_result

inp_list = []

for i in range(0, n):
    inp_list.append(int(input()))
    
for i in range(0, n):
    a, b = map(str, get_fib_count(inp_list[i]))
    print(a + " " + b)