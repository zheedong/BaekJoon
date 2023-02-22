import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = 0
pos_nums = []
neg_nums = []
zeros = 0

for _ in range(n):
    inp = int(input().rstrip())
    if inp == 1:
        answer += 1
    elif inp == 0:
        zeros += 1
    elif inp > 0:
        pos_nums.append(inp)
    elif inp < 0:
        neg_nums.append(inp)

pos_nums.sort(reverse=True)
neg_nums.sort()

if len(pos_nums) % 2 == 1:
    answer += pos_nums[-1]
    pos_nums = pos_nums[:-1]

idx = 0
while idx + 1 < len(pos_nums):
    cur_num = pos_nums[idx]
    next_num = pos_nums[idx + 1]
    answer += cur_num * next_num
    idx += 2

if len(neg_nums) % 2 == 1:
    if zeros == 0:
        answer += neg_nums[-1]
    else:
        zeros -= 1
    neg_nums = neg_nums[:-1]

idx = 0
while idx + 1 < len(neg_nums):
    cur_num = neg_nums[idx]
    next_num = neg_nums[idx + 1]
    answer += cur_num * next_num
    idx += 2

print(answer)

