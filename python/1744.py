import sys
input = sys.stdin.readline

n = int(input().rstrip())
num_lst = []
answer = 0

for _ in range(n):
    inp = int(input().rstrip())
    if inp == 1:
        answer += 1
    else:
        num_lst.append(inp)

num_lst.sort(reverse=True)

idx = 0

for idx in range(0, len(num_lst) - 1, 2):
    cur_num = num_lst[idx]
    next_num = num_lst[idx + 1]

    if cur_num > 0 and next_num > 0: 
        answer += cur_num * next_num
    else:
        break

num_lst = list(reversed(num_lst[idx:]))
print(answer)
print(num_lst)

for idx in range(0, len(num_lst) - 1, 2):
    cur_num = num_lst[idx]
    next_num = num_lst[idx + 1]

    if cur_num < 0 and next_num < 0:
        answer += cur_num * next_num
    else:
        break

num_lst = list(reversed(num_lst[idx:]))
print(answer)
print(num_lst)

