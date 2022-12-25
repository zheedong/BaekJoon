n = int(input())
cycle = 1

def get_cycle(n):
    right_most = str(n)[-1]
    new_num = str(sum(map(int, str(n))))[-1]
    return int(right_most + new_num)

cur_num = get_cycle(n)

while cur_num != n:
    cur_num = get_cycle(cur_num)
    cycle += 1

print(cycle)