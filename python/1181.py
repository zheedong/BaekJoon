test_inp_1 = """
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""

n = int(input())

input_list = []

for i in range(0, n):
    input_list.append(input())
    
no_dup_list = list(set(input_list))

result_list = sorted(no_dup_list, key = lambda x:(len(x), x))

for i in range(0, len(result_list)):
    print(result_list[i])