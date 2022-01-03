from itertools import combinations_with_replacement

n, m = map(int, input().split())

permu_list = list(combinations_with_replacement([i for i in range(1, n+1)], m))
ret_list = permu_list.copy()

if m != 1:
    for permu in permu_list:
        if not all(permu[i] <= permu[i+1] for i in range(len(permu) - 1)):
            ret_list.remove(permu)

for out in ret_list:
    for num in out:
        print(num, end=" ")
    print()