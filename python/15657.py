n, m = map(int, input().split())

inp_list = sorted(list(map(int, input().split())))

def get_not_decrease_permutation(m, nums):
    if m == 0:
        return None
    else:
        res = []
        for i, _ in enumerate(nums):
            try:
                # 일반적인 경우, 한 사이즈 작은 permutation 들을 추가한다.
                for permu in get_not_decrease_permutation(m-1, nums[i:]):
                    res.append([nums[i]] +  permu)
            except:
                # None이 있는 경우, 지금 값만 추가해 준다.
                res.append([nums[i]])
        return res

for permu in get_not_decrease_permutation(m, inp_list):
    # python * 문법
    # 참고 : https://yeomss.tistory.com/160
    print(*permu)