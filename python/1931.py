n = int(input())

conf_set = []

for _ in range(n):
    conf_set.append(tuple(map(int, input().split())))
conf_set.sort()

dp_dict = dict([])
    
def maximum_conf(lst, start_point):
    if len(lst[start_point:]) == 0:
        return 0
    elif len(lst[start_point:]) == 1:
        return 1
    else:
        if start_point in dp_dict:
            return dp_dict[start_point]
        else:
            start_time, end_time = lst[start_point]
            for i in range(start_point, len(lst)):
                next_start, _ = lst[i]
                if next_start >= end_time:
                    break
            ret = 1 + maximum_conf(lst, i)
            dp_dict[start_point] = ret
            return ret
              
ret = 0

for i in range(0, len(conf_set)):
    start, end = conf_set[i]
    for j in range(start, end):
        if j in map(lambda x : x[0] , conf_set):
            buf = maximum_conf(conf_set, j)
            if buf > ret:
                ret = buf
    
print(ret)