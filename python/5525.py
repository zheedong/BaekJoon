n = int(input())
m = int(input())
ioi_str = input()

p_n = "I"
for _ in range(n):
    p_n += "OI"

cnt = 0

for idx in range(m - len(p_n)):
    if ioi_str[idx] == "O":
        continue
    elif ioi_str[idx + 1] == "I":
        continue
    elif p_n == str(ioi_str[idx:idx + len(p_n)]):
        cnt += 1

print(cnt)