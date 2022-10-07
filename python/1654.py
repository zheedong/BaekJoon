k, n = map(int, input().split())

lan_lines = []

for _ in range(k):
    lan_lines.append(int(input()))

lan_lines.sort()

start, end = 1, lan_lines[-1]
max_lan = -1

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan_line in lan_lines:
        cnt += lan_line // mid
    if cnt >= n:
        max_lan = max(max_lan, mid)
        start = mid + 1
    else:
        end = mid - 1
print(max_lan)