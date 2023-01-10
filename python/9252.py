str_1 = list(input())
str_2 = list(input())

lcs = []
for _ in range(len(str_1)):
    lcs.append([0] * (len(str_2)))

for i in range(len(str_1)):
    for j in range(len(str_2)):
        # 같은 문자가 발견되었을 경우
        # 참고해야 하는 str의 index의 주의. 0은 padding이라서 str이 1부터 시작한다고 생각함.
        if str_1[i - 1] == str_2[j - 1]:
            # 지금까지 가장 큰 LCS에서 1을 더한다.
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        # 없다면?
        else:
            # LCS는 연속된 값이 아닐 수도 있다. 그렇기에 지금까지 LCS 값 중에서 가져와야 한다.
            # 예시 : LCS(AB, GBC) = max(LCS(A, GBC), LCS(AB, GB))
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
# LCS string을 만드는 알고리즘도 있지만, 길이를 물어 봐서 가장 마지막 값이 LCS의 길이다.
print(lcs[i][j])