def sol():
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    if n == 1:
        return nums[0]
    min_sum = 99999999
    min_rep = None

    for rep_num in range(nums[0], nums[-1] + 1):

        for idx in range(n):
            if nums[idx] > rep_num:
                break

        cur_sum = (rep_num * idx - sum(nums[:idx])) + (sum(nums[idx:]) - rep_num * (n - idx))

        if min_rep == None:
            min_sum = cur_sum
            min_rep = [rep_num]
            continue

        if min_sum == cur_sum:
            min_rep.append(rep_num)
        elif min_sum > cur_sum:
            min_sum = cur_sum
            min_rep = [rep_num]

    return min_rep[0]

print(sol())