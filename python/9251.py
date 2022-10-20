# LCS
# https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

str_1 = list(input())
str_2 = list(input())

'''
tc1 = ['A', 'C', 'A', 'Y', 'K', 'P']
tc2 = ['C', 'A', 'P', 'C', 'A', 'K']
str_1 = tc1
str_2 = tc2
'''

lcs = []
for _ in range(len(str_1) + 1):
    lcs.append([0] * (len(str_2) + 1))

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif str_1[i - 1] == str_2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
print(lcs[i][j])