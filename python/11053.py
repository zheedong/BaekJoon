n = int(input())
inp_list = list(map(int, input().split()))

# Index를 넣으면 그 idx에서 최대 길이를 출력함.
dyn_idx_length = dict([])

def solution(idx):
    # Dynamic Programming
    try:
        # 먼저 이미 알고 있던 값인지 확인한다.
        return dyn_idx_length[idx]
    except:
        # 초기값은 1.
        dyn_idx_length[idx] = 1
        # 가능한 모든 next index 중
        for next_idx in range(idx + 1, len(inp_list)):
            # 오직 지금 값보다 큰 경우 (증가하는 경우)에만
            if inp_list[next_idx] > inp_list[idx]:
                # 현재보다 길이가 길어지는 경우를 업데이트 해 준다.
                dyn_idx_length[idx] = max(dyn_idx_length[idx], solution(next_idx) + 1)
        return dyn_idx_length[idx]

max_length = 0
# 시작 점을 0이 아니라 모든 곳에서 확인해 준다.
for i, _ in enumerate(inp_list):
    max_length = max(solution(i), max_length)
print(max_length)