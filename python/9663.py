n = int(input())

def nqueen(row, pos, visitied, n):
    count = 0
    if row == n:    # If all row passed.
        return 1
    for col in range(n):    # Check all col
        if visitied[col]:   # If col is already visited then pass.
            continue
        pos[row] = col      # pos get row and return col where queen is in.
        for i in range(row):    # Check diagnal.
            if abs(i - row) == abs(pos[i] - pos[row]):  # If base (pos[i] - pos[row]) and height (abs(i - row)) is same, it's in diagnal.
                break
        else:               # for ... else. Only loop doesn't end as 'break' i.e. possible queen case
            visitied[col] = True
            count += nqueen(row + 1, pos, visitied, n)  # Update the visitied and recursive call
            visitied[col] = False   # Then, reset the state of visitied node.
    return count

print(nqueen(0, [0] * n, [False] * n, n))