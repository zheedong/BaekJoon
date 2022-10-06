n, m, b = map(int, input().split())

inp_lst = []

for _ in range(n):
    row = list(map(int, input().split()))
    inp_lst += row
    # 2D로 생각할 필요가 없기 때문에 1D로 만들어서 풀어도 된다.

inp_lst.sort(reverse=True)
max_inp, min_inp = inp_lst[0], inp_lst[-1]

min_time = 1000000000
max_height = -1

# 최대 높이의 한계가 가장 큰 값에서부터 시작해서 하나씩 줄어든다.
for cur_max_height in range(max_inp, min_inp - 1, -1):
    cur_lst = inp_lst
    # Block들은 높이가 내림차순으로 정렬되어 있다.
    cur_inventory = b
    cur_time = 0

    # max height 보다 큰 블록을 모두 제거하고, min height 보다 작은 블록을 모두 추가한다.
    # 이 때, 인벤토리에 블록을 추가할 때는 2배의 시간이 소요된다. 
    for block in cur_lst:
        # 먼저 block을 제거하는 경우를 시도한다 (inventory에 먼저 추가되어야 하기 때문이다.)
        if block > cur_max_height:
            cur_inventory += (block - cur_max_height)
            cur_time += (block - cur_max_height) * 2
        elif block < cur_max_height:
            cur_inventory -= (cur_max_height - block)
            # 인벤토리가 부족하면 불가능한 경우이다.
            if cur_inventory < 0:
                continue
            cur_time += (cur_max_height - block)

    if cur_inventory < 0:
        continue
    elif min_time > cur_time:
        min_time = cur_time
        max_height = cur_max_height

print(min_time, max_height)