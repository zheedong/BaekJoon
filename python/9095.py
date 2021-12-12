t = int(input())

score_dict = dict([])
score_dict[0] = 1
score_dict[1] = 1
score_dict[2] = 2

def get_score(n):
    if n in score_dict:
        return score_dict[n]
    else:
        sum_n_3 = 0
        for i in range(n-2):
            sum_n_3 += get_score(i)
        
        ret = 1 + get_score(n-2) + 2 * sum_n_3
        # Same as 1 + sum_n_2 + sum_n_3
        score_dict[n] = ret
        return ret
    
    
inp_list = []

for i in range(t):
    inp_list.append(int(input()))
    
for n in inp_list:
    print(get_score(n))