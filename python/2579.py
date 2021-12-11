n = int(input())

score = dict([])
max_dict = dict([])

for i in range(1, n + 1):
    score[i] = int(input())

# max(n) = max(max(n-2), max(n-3) + score(n-1)) + score(n)
# Key IDEA : 맨 끝 계단을 밟아야 한다는 조건에 주목. 그러기 위해서는 두 가지 선택지 밖에 없음
# Dynamic Programming과 Recursion을 활용해서 해결. => n보다 작은 수에서는 작동하는 함수가 있다고 가정. (SICP)
def get_max(n):
    if n in max_dict:
        return max_dict[n]
    else:
        ret = max(get_max(n-2), get_max(n-3) + score[n - 1]) + score[n]
        max_dict[n] = ret
        return ret
    
if n >= 1:
    max_dict[1] = score[1]
if n >= 2:
    max_dict[2] = score[1] + score[2]
if n >= 3:
    max_dict[3] = max(score[1], score[2]) + score[3]
if n >= 4:
    get_max(n) 
    
print(max_dict[n])