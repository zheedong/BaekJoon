n, s = map(int, input().split())
num_array = list(map(int, input().split()))

# 누적 합
for i in range(1, n):
    num_array[i] += num_array[i - 1]
num_array = [0] + num_array

start = 0
end = 0 
min_length = int(1e9)
is_found = False

# Sum i to j
def get_part_sum(arr, i, j):
    return arr[j + 1] - arr[i]

# print(num_array)
interval_sum = 0

# Two - pointer 첫경험
for start in range(n):
    interval_sum = get_part_sum(num_array, start, end)
    # print(f"New Start : {start}, Cur End : {end} || {interval_sum}")
    flag = False
    while interval_sum < s and end < n - 1:
        end += 1
        interval_sum = get_part_sum(num_array, start, end)
        # print(f"Start : {start}, End : {end} || {interval_sum}")

    # 조건이 '이상'이었다... 눈을 크게 뜨자 제발
    if interval_sum >= s:
        min_length = min(min_length, end - start + 1)
        # print(f"{start}, {end}, Update : {min_length}")

if min_length == int(1e9):
    print(0)
else:
    print(min_length)
