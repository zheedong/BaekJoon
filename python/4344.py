c = int(input())
for _ in range(c):
    inp = list(map(int, input().split()))
    n = inp[0]
    inp = inp[1:]
    mean = sum(inp) / n

    cnt = 0
    for student in inp:
        if student > mean:
            cnt += 1
    print(f"{100 * cnt / n:.3f}%")