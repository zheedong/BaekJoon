from itertools import combinations
l, c = map(int, input().split())
inp = sorted(list(input().split()))
collection = set(['a', 'e', 'i', 'o', 'u'])
for ans in list(combinations(inp, l)):
    if len(set(ans).intersection(collection)) >= 1 and len(set(ans).difference(collection)) >= 2:
        print("".join(ans))