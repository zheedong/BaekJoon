# 구조를 잘 살피니... 뜻밖의 피보나치 수열!!

n = int(input())

nth_fibb = dict([])
nth_fibb[0] = 1
nth_fibb[1] = 1

def get_nth_fibb(n):
    if n in nth_fibb:
        return nth_fibb[n]
    else:
        ret = get_nth_fibb(n - 2) + get_nth_fibb(n - 1)
        nth_fibb[n] = ret
        return ret

print(get_nth_fibb(n) % 10007)