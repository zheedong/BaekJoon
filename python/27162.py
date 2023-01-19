# Board Game Cup D

choice_able = [None] + list(input())
cur_dice = list(map(int, input().split()))
max_score = -1

for idx, flag in enumerate(choice_able):
    if idx == 0:
        continue
    elif idx >= 1 and idx <= 6 and flag == "Y":
        buf = cur_dice.count(idx)
        max_score = max(max_score, ((buf + 2) * 1))
    elif idx == 8 and flag == "Y":
        for i in range(1, 7):
            if cur_dice.count(i) >= 2:
                max_score = max(max_score, i * 4)


