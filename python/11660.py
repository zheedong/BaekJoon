import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cost_matrix = []

for _ in range(n):
    cost_matrix.append(list(map(int, input().split())))

'''
tc1_n, tc1_m = 4, 3
tc1_cost = [[1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7]]

n, m = tc1_n, tc1_m
cost_matrix = tc1_cost
'''

# 첫 번째 row와 col에 0으로 padding을 넣어준다.
def add_padding(mat):
    n = len(mat)
    for idx, row in enumerate(mat):
        mat[idx] = [0] + row
    mat.insert(0, [0] * (n + 1))
    return mat

# 누적 합 list 만들기
def get_sum_list(arr):
    n = len(arr)
    # row의 합
    sum_list = [[sum(arr[row][:col + 1]) for col in range(n)] for row in range(n)]

    # row의 합을 위에서부터 합해주기
    for i in range(len(sum_list) - 1):
        for j in range(len(sum_list[0])):
            sum_list[i + 1][j] += sum_list[i][j]
    return sum_list

# 누적 합 알고리즘
def get_accum(sum_list, coordi1, coordi2):
    x1, y1 = map(lambda x : x - 1, coordi1)
    x2, y2 = coordi2
    return sum_list[x2][y2] - sum_list[x1][y2] - sum_list[x2][y1] + sum_list[x1][y1]

sum_list = get_sum_list(add_padding(cost_matrix))

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(get_accum(sum_list, (x1, y1), (x2, y2)))