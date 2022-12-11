import sys
input = sys.stdin.readline

m = int(input().rstrip())

# We don't need to save real list.
a_sum = 0
a_xor = 0

for _ in range(m):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        a_sum += inp[1]
        a_xor ^= inp[1]
    elif inp[0] == 2:
        a_sum -= inp[1]
        a_xor ^= inp[1]
    elif inp[0] == 3:
        sys.stdout.write(f"{a_sum}\n")
    else:
        sys.stdout.write(f"{a_xor}\n")