import math
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def get_divisor(n):
    ret = set([])
    ret = set([])
    for i in range(1, round(math.sqrt(n)) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    ret = sorted(list(ret))
    return ret

# less, over, same = 0 1 2

def check_over_less(n):
    num = sum(get_divisor(n)[:-1])
    if num < n:
        return 0
    elif num > n:
        return 1
    else:
        return 2

for _ in range(t):
    n = int(input().rstrip())
    print(get_divisor(n))
    if check_over_less(n) == 1:
        for num in get_divisor(n)[:-1]:
            print(f"num : {num}, Check : {check_over_less(num)}")
            if check_over_less(num) == 1:
                print("BOJ 2022")
                break
        else:
            print("Good Bye")
    else:
        print("BOJ 2022")
