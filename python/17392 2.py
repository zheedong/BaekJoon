n, m = map(int, input().split())
happy = list(map(lambda x: int(x) + 1, input().split()))

def get_square_sum(x):
    nums = [i ** 2 for i in range(1, x+1)]
    return sum(nums)

total = 0
unhappy_days = m - sum(happy)

if unhappy_days <= 0:
    print(total)
else:
    # unhappy_days를 n에 나눠서 느껴야 한다.
    # 10 to 3
    depress_list = [0 for _ in range(n)]
    for i in range(unhappy_days):
        depress_list[i % (n)] += 1
    print(depress_list)
    print(sum(list(map(lambda x: get_square_sum(x), depress_list))))

# 3 10
# 1 1 1
# 4 to 3
# 1 0 {-1 -2} 1 0 {-1} 1 0 {-1}
