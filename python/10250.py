test_case_1 = """
2
6 12 10
30 50 72
"""
max_loop = int(input())

for i in range(0, max_loop):
    H, W, N = map(int, input().split())
    result, rest = divmod(N, H)
    if rest == 0:
        print(str(H)+str(result).zfill(2))
    else:
        print(str(rest)+str(result+1).zfill(2))
        