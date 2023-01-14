# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

str_1 = [None] + list(input())
str_2 = [None] + list(input())

lcs = []
for _ in range(len(str_1)):
    lcs.append([0] * (len(str_2)))

for i in range(len(str_1)):
    for j in range(len(str_2)):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif str_1[i] == str_2[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[i][j])

i = len(str_1) - 1
j = len(str_2) - 1
result = []
while True:
    if lcs[i][j] == 0:
        break
    elif lcs[i][j] == lcs[i - 1][j]:
        i -= 1
    elif lcs[i][j] == lcs[i][j - 1]:
        j -= 1
    else:
        result.append(str_1[i])
        i -= 1
        j -= 1
result.reverse()

print("".join(result))
