n = int(input())
a_list = list(map(lambda x: {int(x)}, input().split()))
a_list.sort(key=lambda x: sum(x))

def get_ans_idx(a_list):
    k = len(a_list)
    return ((k + 1) // 2) - 1

def get_score(a_list):
    k = len(a_list)
    return sum(a_list[get_ans_idx(a_list)]) / len(a_list[get_ans_idx(a_list)])

while get_ans_idx(a_list) > 