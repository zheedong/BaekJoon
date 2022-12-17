import sys
input = sys.stdin.readline

w, h, n = map(int, input().split())
dest_list = []
for _ in range(n):
    x, y = map(int, input().split())
    dest_list.append((x, y))

def get_path(start, end):
    x1, y1 = start
    x2, y2 = end
    vec1, vec2 = (x2 - x1), (y2 - y1)
    if vec1 * vec2 > 0:
        return max(abs(vec1), abs(vec2))
    else:
        return abs(vec1) + abs(vec2)

start = dest_list[0]
min_path = 0
for end in dest_list[1:]:
    min_path += get_path(start, end)
    start = end

print(min_path)