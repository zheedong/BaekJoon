n = int(input())
m = int(input())

useable_button = set([i for i in range(0, 10)])
# 고장난 버튼이 없는 경우 broken button 입력을 받지 않는다.
if m != 0:
    broken_button = set(map(int, input().split()))
    useable_button -= broken_button

# 현재 채널이 사용 가능한 버튼들 만을 이용해 만들 수 있는지 계산한다.
def check_all_num_usable(channel, useable_button):
    if set(map(int, str(channel))) - useable_button:
        return False
    else:
        return True

if m == 10:
    # 전부 고장난 경우 + / - 버튼만 사용할 수 있다.
    res = abs(n - 100)
elif useable_button == set([0]):
    # 사용 가능한 버튼이 0만 있는 경우는 특수하게 처리.
    # 반례
    # 1
    # 9
    # 1 2 3 4 5 6 7 8 9
    # 답 : 2
    # 0에서부터 찾아가기 vs 100에서부터 찾아가기. 0에서 찾아갈 경우 0을 누르는 클릭 1을 더해줘야 한다.
    res = min(n + 1, abs(n - 100))
else:
    # 한 방향으로만 증가하는 변수 두 개 선언
    only_inc = only_dec = n
    # 처음 입력하는 번호의 길이
    inc_init_length = dec_init_length = 0
    inc_cnt = dec_cnt = 0

    while(True):
        if check_all_num_usable(only_inc, useable_button):
            inc_init_length = len(str(only_inc))
            break
        else:
            only_inc += 1
            inc_cnt += 1

    # 증가하는 쪽에서 먼저 답을 찾더라도, dec에서 처음 입력하는 숫자 길이의 차이로 더 작은 값이 생길 수도 있다. 따로 계산해 줘야 한다.
    # 반례
    # 1555
    # 8
    # 0 1 3 4 5 6 7 9
    # 답 : 670
    while(True):
        # 채널은 0보다 작을 수 없다.
        if only_dec < 0:
            break
        elif check_all_num_usable(only_dec, useable_button):
            dec_init_length = len(str(only_dec))
            break
        else:
            only_dec -= 1
            dec_cnt += 1

    # 처음 입력해야 하는 채널 값 + (+ / -) 를 누른 횟수.
    # 초기값 100에서 + / - 버튼만 사용한 경우가 더 적을 수도 있다.
    if only_dec < 0:
        res = min(inc_init_length + inc_cnt, abs(n - 100))
    else:
        res = min(inc_init_length + inc_cnt, dec_init_length + dec_cnt, abs(n - 100))

print(res)