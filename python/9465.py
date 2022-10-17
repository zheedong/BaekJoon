import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t_case_num = int(input())
# t_case_num = 1

UP_ROW = 0
DOWN_ROW = 1
NO_CHOICE = 2
CHOICES = [UP_ROW, DOWN_ROW, NO_CHOICE]

# Naive 재귀 Ver.
def naive_rec(prev_choice, cur_col):
    # 가능한 prev_choice의 경우는 3가지. UP Row, Down Row, NO_CHOICE
    cur_max = -1
    for cur_choice in CHOICES:
        if cur_choice == prev_choice:
            continue
        elif cur_choice == NO_CHOICE:
            cur_max = max(cur_max, (0 if cur_col == n - 1 else naive_rec(cur_choice, cur_col + 1)))
        else:
            cur_max = max(cur_max, sticker[cur_choice][cur_col]+ (0 if cur_col == n - 1 else naive_rec(cur_choice, cur_col + 1)))
    return cur_max

# Dynamic Programming Ver.
def dp_solution(prev_choice, cur_col):
    cur_max = -1
    for cur_choice in CHOICES:
        if not dp_score[cur_choice][cur_col] == None:
            cur_score = dp_score[cur_choice][cur_col]
        else:
            cur_score = 0
            cur_score += 0 if cur_choice == NO_CHOICE else sticker[cur_choice][cur_col]
            cur_score += 0 if cur_col == n - 1 else dp_solution(cur_choice, cur_col + 1)
            dp_score[cur_choice][cur_col] = cur_score

        if cur_choice == prev_choice:
            continue
        else:
            cur_max = max(cur_max, cur_score)

    return cur_max

for _ in range(t_case_num):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))

    '''
    # Test Cases
    tc1 = [[50, 10, 100, 20, 40],
           [30, 50, 70,  10, 60]]
    tc1_n = 5
    # ans = 260

    tc2 = [[10], [20]]
    tc2_n = 1

    tc3 = [[10, 30, 10, 50, 100, 20, 40]
          ,[20, 40, 30, 50, 60, 20, 80]]
    tc3_n = 7
    # ans = 290

    sticker = tc2
    n = tc2_n
    '''

    # Dynamic Programming
    # Key = [cur_choice][cur_col] | Value = score
    # dict로 구현하니 메모리 문제가 발생. 이중 리스트로 바꿈.
    # 그래도 여전히 Pypy로는 풀 수 없다...
    dp_score = [[], [], []]
    for row in dp_score:
        for _ in range(n):
            row.append(None)

    # print(naive_rec(NO_CHOICE, 0))
    print(dp_solution(NO_CHOICE, 0))