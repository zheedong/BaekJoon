import math
n = int(input())

# n을 k개의 제곱수의 합으로 나타낼 수 있는가?
def is_n_sum_of_k_squares(n, k):
    square_n = int(math.sqrt(n))
    # Base Case k == 1
    if k == 1:
        if square_n ** 2 == n:
            return True
    elif k > 1:
        flag = False
        for cur_poss in range(square_n, 0, -1):
            flag = flag | is_n_sum_of_k_squares(n - (cur_poss ** 2), k - 1)
        return flag
    return False

k = 1
while(True):
    if is_n_sum_of_k_squares(n, k):
        print(k)
        break
    else:
        k += 1