import math

# 좌표가 row, col로 주어지는데 이걸 생각 안 하고 해서 수많은 버그를 만났다... 디버깅이 힘들었던 문제 (1시간 50분 컷ㅋㅋ)
# Divide and Conquer은 쉽게 알 수 있다

n, r, c = map(int, input().split())

def check_quadrant(n, r, c):
    check_stan = math.pow(2, n - 1)
    
    if  r < check_stan:
        if c < check_stan:
            return 0
        else:
            return 1
    else:
        if c < check_stan:
            return 2
        else:
            return 3
            
def get_num(target_coordi, n):
    r, c = target_coordi
    if n == 1:
        if r % 2 == 0:
            if c % 2 == 0:
                return 0
            else:
                return 1
        else:
            if c % 2 == 0:
                return 2
            else:
                return 3
    else:
        new_quadrant = check_quadrant(n, r, c)
        new_start = new_quadrant * math.pow(2, 2 * n - 2)
        
        # 문제 크기 감소에 따른 좌표 평행 이동
        
        if new_quadrant == 0:
            new_r = r
            new_c = c
        elif new_quadrant == 1:
            new_r = r
            new_c = c - math.pow(2, n - 1)
        elif new_quadrant == 2:
            new_r = r - math.pow(2, n - 1)
            new_c = c
        elif new_quadrant == 3:
            new_r = r - math.pow(2, n - 1)
            new_c = c - math.pow(2, n - 1)
            
        return new_start + get_num((new_r, new_c), n - 1)        # 재귀할 때, 재귀로 들어가기 전까지의 값과, 문제의 사이즈가 1/4이 됐다 생각 했을 때 값을 더해준다
    
print(int(get_num((r, c), n)))