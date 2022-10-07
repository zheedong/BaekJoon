n, m = map(int, input().split())

tree_height_list = list(map(int, input().split()))

start, end = 0, max(tree_height_list)
cutter_max_height = -1

while start <= end:
    mid = (start + end) // 2
    length = 0
    for tree in tree_height_list:
        length += max(0, (tree - mid))
    if length >= m:
        cutter_max_height = max(mid, cutter_max_height)
        start = mid + 1
    else:
        end = mid - 1
print(cutter_max_height)