n = int(input())

conf_set = []

for _ in range(n):
    conf_set.append(tuple(map(int, input().split())))
conf_set.sort(key=lambda x : (x[1], x[0]))
# 끝나는 시간을 기준으로 정렬
# 시작과 종료가 같은 경우를 포함하기 위해선, 시작 시간도 오름차순으로 정렬해 줘야 한다

solution_list = [conf_set[0]]

# Greedy Algorithm

for conf in conf_set[1:]:
    last_conf = solution_list[-1]
    _, last_end_time = last_conf
    new_start_time, _ = conf
    
    # 정렬된 회의의 list의 마지막 값의 시작 시간과, 정답 list 마지막의 종료 시간을 비교한다
    if new_start_time >= last_end_time:
        solution_list.append(conf)

print(len(solution_list))