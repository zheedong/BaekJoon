test_input_1 = """\
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
"""

test_input_2 = """\
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""

test_input_3 = """\
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
"""

test_input_4 = """\
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
"""

# ERROR CASE
test_input_7 = """\
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
"""

START_WITH_B = "BWBWBWBW"
START_WITH_W = "WBWBWBWB"

def get_count_diff_two_length8_string(str1, str2):
    count = 0
    for i in range(0,8):
        if str1[i] != str2[i]:
            count += 1
    return count

M, N = input().split()
M, N = map(int, (M, N))

input_array = []

for i in range(0, M):
    input_array.append(input())

number_of_possible_case = (M-7) * (N-7)

MAX = 100000000000
min_upperleft_black_counter = MAX
min_upperleft_white_counter = MAX

flag = True

for i in range(0, M-7):
    test_board = input_array[i:i+8]
    
    for j in range(0, N-7):
        upperleft_black_counter = 0
        upperleft_white_counter = 0
        for row in range(0, 8):
            if flag == True:
                upperleft_black_counter += get_count_diff_two_length8_string(START_WITH_B, test_board[row][j:j+8])
                upperleft_white_counter += get_count_diff_two_length8_string(START_WITH_W, test_board[row][j:j+8])
            else:
                upperleft_white_counter += get_count_diff_two_length8_string(START_WITH_B, test_board[row][j:j+8])
                upperleft_black_counter += get_count_diff_two_length8_string(START_WITH_W, test_board[row][j:j+8])
            flag = not(flag)
            
        if min_upperleft_black_counter > upperleft_black_counter:
            min_upperleft_black_counter = upperleft_black_counter
        if min_upperleft_white_counter > upperleft_white_counter:
            min_upperleft_white_counter = upperleft_white_counter
        
if min_upperleft_black_counter > min_upperleft_white_counter:
    print(min_upperleft_white_counter)
else:
    print(min_upperleft_black_counter)