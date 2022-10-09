n = int(input())

paper_mat = []

for _ in range(n):
    paper_mat.append(list(map(int, input().split())))

'''
# Test Case
tc1_mat = [[0, 0, 0, 1, 1, 1,-1,-1,-1,],
           [0, 0, 0, 1, 1, 1,-1,-1,-1,],
           [0, 0, 0, 1, 1, 1,-1,-1,-1,],
           [1, 1, 1, 0, 0, 0, 0, 0, 0,],
           [1, 1, 1, 0, 0, 0, 0, 0, 0,],
           [1, 1, 1, 0, 0, 0, 0, 0, 0,],
           [0, 1,-1, 0, 1,-1, 0, 1,-1,],
           [0,-1, 1, 0, 1,-1, 0, 1,-1,],
           [0, 1,-1, 0, 1,-1, 0, 1,-1,]]
tc2_mat = [[0]]
'''

# matrix를 9등분해서 array로 리턴
def matrix_div_9(mat):
    size_n = len(mat)
    target_size = size_n // 3
    ret_met = []
    for j in range(0, size_n, target_size):
        for i in range(0, size_n, target_size):
            ret_met.append([row[i:i+target_size] for row in mat[j:j+target_size]])
    return ret_met

# matrix 내부의 값이 모두 같은지 확인
def is_all_same(mat):
    init = mat[0][0]
    flag = True
    for row in mat:
        for col in row:
            flag = flag & (init == col)
    return flag
            
# 각 값들의 count를 저장함
cnt = dict()
cnt[-1] = 0
cnt[0] = 0
cnt[1] = 0

def solution(mat):
    if is_all_same(mat):
        cnt[mat[0][0]] += 1
        return
    else:
        for divied_mat in matrix_div_9(mat):
            solution(divied_mat)

solution(paper_mat)
print(cnt[-1])
print(cnt[0])
print(cnt[1])