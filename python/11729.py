ret = []

def hanoi(n, start, end, mid):
    if n == 1:
        ret.append((start, end))
        return
    else:
        hanoi(n - 1, start, mid, end)
        hanoi(1, start, end, mid)
        hanoi(n - 1, mid, end, start)

n = int(input())
hanoi(n, 1, 3, 2)
print(len(ret))
for process in ret:
    print(*process)