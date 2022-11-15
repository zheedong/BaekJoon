import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input().rstrip())
    ret = 0
    for _ in range(n):
        ret += int(input().rstrip())
    print(0 if ret == 0 else "+" if ret > 0 else "-")