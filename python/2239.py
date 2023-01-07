inp = []
for _ in range(9):
    inp.append(list(map(int, list(input()))))

def get_poss_num(ri, ci):
    poss_set = set([i for i in range(1, 10)])
    # 1. Check row
    for num in inp[ri]:
        try:
            poss_set.remove(num)
        except:
            continue
    # 2. Check col
    for row in inp:
        try:
            poss_set.remove(row[ci])
        except:
            continue
    # 3. Check square
    for i in range(3):
        for j in range(3):
            try:
                poss_set.remove(inp[3 * (ri // 3) + i][3 * (ci // 3) + j])
            except:
                continue
    return list(poss_set)

# One or more possible case.
flag = False

def sudoku():
    global flag
    if flag:
        return
    global inp
    for row_idx, row in enumerate(inp):
        for col_idx, col in enumerate(row):
            if col == 0:
                for num in get_poss_num(row_idx, col_idx):
                    # Backtracking
                    inp[row_idx][col_idx] = num
                    sudoku()
                    inp[row_idx][col_idx] = 0
                else:
                    return
    else:
        flag = True
        for row in inp:
            row = list(map(str, row))
            print("".join(row))

sudoku()
