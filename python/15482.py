str1 = list(input())
str2 = list(input())

lcs_mat = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

for i in range(len(str2) + 1):
    for j in range(len(str1) + 1):
        if i == 0 or j == 0:
            lcs_mat[i][j] = 0
        elif str1[j - 1] == str2[i - 1]:
            lcs_mat[i][j] = lcs_mat[i - 1][j - 1] + 1
        else:
            lcs_mat[i][j] = max(lcs_mat[i - 1][j], lcs_mat[i][j - 1])

print(lcs_mat[i][j])
            

