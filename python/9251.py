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
        # 0 번째 row, col은 padding. 사용하지 않는다.
        if i == 0 or j == 0:
            lcs[i][j] = 0
        # 같은 문자가 발견되었을 경우
        # 참고해야 하는 str의 index의 주의. 0은 padding이라서 str이 1부터 시작한다고 생각함.
        elif str_1[i - 1] == str_2[j - 1]:
            # 지금까지 가장 큰 LCS에서 1을 더한다.
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        # 없다면?
        else:
            # LCS는 연속된 값이 아닐 수도 있다. 그렇기에 지금까지 LCS 값 중에서 가져와야 한다.
            # 예시 : LCS(AB, GBC) = max(LCS(A, GBC), LCS(AB, GB))
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
# LCS string을 만드는 알고리즘도 있지만, 길이를 물어 봐서 가장 마지막 값이 LCS의 길이다.
print(lcs[i][j])