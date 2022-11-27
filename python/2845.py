l, p = map(int, input().split())
people_nums = list(map(int, input().split()))
print(*list(map(lambda x : x - (l * p), people_nums)))