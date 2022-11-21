ans = [1, 1, 2, 2, 2, 8]
inp = list(map(int, input().split()))
print(*[ans[idx] - inp[idx] for idx, _ in enumerate(ans)])