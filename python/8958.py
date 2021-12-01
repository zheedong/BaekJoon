test_case_1 = """
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
"""

def sigma(n):
    return (n * n + n)/2

def get_score(str):
    str_length = len(str)
    score = 0
    o_counter = 0
    
    for i in range(0, str_length):
        target_char = str[i]
        if target_char == 'O':
            o_counter += 1
        else:
            score += sigma(o_counter)
            o_counter = 0
    score += sigma(o_counter)
    return int(score)
        
n = int(input())

for i in range(0, n):
    print(get_score(input()))