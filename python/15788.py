import sys
input = sys.stdin.readline

n = int(input())
puzzle = []

for _ in range(n):
    puzzle.append(list(map(int, input().split())))

def get_expected_sum(puzzle):
    for row in puzzle:
        if 0 not in row:
            return sum(row)

def check_rule1(puzzle, expected_sum):
    sum_except_m = None
    for row in puzzle:
        if 0 in row:
            sum_except_m = sum(row)
        else:
            if expected_sum != sum(row):
                return -1
    else:
        return expected_sum - sum_except_m

# fancy way to transpose matrix
def transpose(mat):
    return list(map(list, zip(*mat)))

def check_rule2(puzzle, expected_sum):
    return check_rule1(transpose(puzzle), expected_sum)

def check_rule3(puzzle, expected_sum):
    diag1 = [puzzle[i][j] for i, j in zip(range(n), range(n))]
    diag2 = [puzzle[i][j] for i, j in zip(range(n), reversed(range(n)))]
    # two zeros
    if 0 in diag1 and 0 in diag2:
        if not (sum(diag1) == sum(diag2)):
            return -1
        else:
            return None
    # one zero (same situation)
    elif 0 in diag1 or 0 in diag2:
        return check_rule1([diag1, diag2], expected_sum)
    # no zero
    else:
        if not (sum(diag1) == sum(diag2)):
            return -1
        else:
            return None

def sol(puzzle):
    expected_sum = get_expected_sum(puzzle)
    rule1 = check_rule1(puzzle, expected_sum)
    rule2 = check_rule2(puzzle, expected_sum)
    rule3 = check_rule3(puzzle, expected_sum)

    if rule3:
        if rule1 == rule2 == rule3:
            return rule1
    else:
        if rule1 == rule2:
            return rule1
    return -1

print(sol(puzzle))