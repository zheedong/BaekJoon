import sys
input = sys.stdin.readline

n = int(input())

# 지금까지의 max 값이 저장된 list와 next_row의 값들 중, 조건을 만족시키며 더하게 한다.
# 리펙토링 할 수 있을꺼 같은데 일단 넘어가자...
def memory_save_max(cur_max_row, next_row):
    next_max_row = [0, 0, 0]
    next_max_row[0] = next_row[0] + max(cur_max_row[0], cur_max_row[1])
    next_max_row[1] = next_row[1] + max(cur_max_row[0], cur_max_row[1], cur_max_row[2])
    next_max_row[2] = next_row[2] + max(cur_max_row[1], cur_max_row[2])
    return next_max_row

def memory_save_min(cur_min_row, next_row):
    next_min_row = [0, 0, 0]
    next_min_row[0] = next_row[0] + min(cur_min_row[0], cur_min_row[1])
    next_min_row[1] = next_row[1] + min(cur_min_row[0], cur_min_row[1], cur_min_row[2])
    next_min_row[2] = next_row[2] + min(cur_min_row[1], cur_min_row[2])
    return next_min_row

first_row = list(map(int, input().split()))
cur_max_row = cur_min_row = first_row

# 입력을 한 줄 씩 받아서 처리한다. 밑이나 위의 정보를 다 저장하고 있을 필요가 없기 때문에.
for _ in range(n - 1):
    next_row = list(map(int, input().split()))
    # 마지막 줄에 왔으면 break
    if not next_row:
        break
    cur_max_row = memory_save_max(cur_max_row, next_row)
    cur_min_row = memory_save_min(cur_min_row, next_row)

print(*(max(cur_max_row), min(cur_min_row)))

# ---- 밑은 장렬한 삽질의 현장... ----
sys.setrecursionlimit(10 ** 8)
INF = 10 ** 10
game_board = []

# 실패한 이유 : int를 10만개 받으면 이미 4MB 제한을 넘어간다.
'''
for _ in range(n):
    game_board.append(list(map(int, input().split())))
'''

def get_poss_next_choice(n):
    if n == 0:
        return [0, 1]
    elif n == 1:
        return [0, 1, 2]
    else:
        return [1, 2]

# prev_choice가 좌표라고 생각
# 초기 값을 (-1, choice)로 줘야 한다.
def get_solution(game_board, sol_func):
    max_lst = []
    min_lst = []
    for i in [0, 1, 2]:
        max_var, min_var = sol_func((-1, i), game_board)
        max_lst.append(max_var)
        min_lst.append(min_var)
    return max(max_lst), min(min_lst)

def naive_rec(prev_coordi, game_board):
    max_cur = -1
    min_cur = INF

    prev_row, prev_choice = prev_coordi
    cur_row = prev_row + 1
    last_row = len(game_board) - 1

    for cur_choice in get_poss_next_choice(prev_choice):
        max_next, min_next = (0, 0) if cur_row == last_row else naive_rec((cur_row, cur_choice), game_board)
        max_cur = max(max_cur, game_board[cur_row][cur_choice] + max_next)
        min_cur = min(min_cur, game_board[cur_row][cur_choice] + min_next)
    return max_cur, min_cur

# 늘 하던대로 DP... 인 줄 알았지만
position_to_max_min_score = [[None]*n for _ in range(n)]

def dp_solution(prev_coordi, game_board):
    max_cur = -1
    min_cur = INF

    prev_row, prev_choice = prev_coordi
    cur_row = prev_row + 1
    last_row = len(game_board) - 1

    for cur_choice in get_poss_next_choice(prev_choice):
        if position_to_max_min_score[cur_row][cur_choice] != None:
            cur_choice_max, cur_choice_min = position_to_max_min_score[cur_row][cur_choice]
        else:
            max_next, min_next = (0, 0) if cur_row == last_row else dp_solution((cur_row, cur_choice), game_board)
            cur_choice_max = game_board[cur_row][cur_choice] + max_next
            cur_choice_min = game_board[cur_row][cur_choice] + min_next
            position_to_max_min_score[cur_row][cur_choice] = (cur_choice_max, cur_choice_min)
        max_cur = max(max_cur, cur_choice_max)
        min_cur = min(min_cur, cur_choice_min)
    return max_cur, min_cur

# print(*get_solution(game_board, naive_rec))
# print(*get_solution(game_board, dp_solution))