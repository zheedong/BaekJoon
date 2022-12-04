n = int(input())

def check_is_han(num):
    num_list = list(map(int, str(num)))
    if len(num_list) == 1:
        return True
    else:
        d = num_list[1] - num_list[0]
        inc_num = [num_list[0]]
        for _ in range(len(num_list) - 1):
            inc_num.append(inc_num[-1] + d)
        if num_list == inc_num:
            return True
        else:
            return False

cnt = 0

for cur_num in range(1, n + 1):
    if check_is_han(cur_num):
        cnt += 1

print(cnt)