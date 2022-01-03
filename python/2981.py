import sys

n = int(input())
inp_list = []

for _ in range(n):
    inp_list.append(int(sys.stdin.readline().strip()))
    
def solution(num_list):
    if len(num_list) == 2:
        a_0 = num_list[0]
        a_1 = num_list[1]
        return_set = set([])
        for try_num in range(2, a_0 + 1):
            if a_0 % try_num == a_1 % try_num:
                return_set.add(try_num)
        return list(return_set)
    else:
        smallest = num_list[0]
        rec_res_list = solution(num_list[1:])
        return_set = set(rec_res_list)
        for num in rec_res_list:
            if smallest % num != num_list[1] % num:
                return_set.remove(num)
        return list(return_set)
        
sol = sorted(solution(inp_list))

for num in sol:
    print(num, end = " ")
print()