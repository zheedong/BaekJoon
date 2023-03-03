from math import log2
from copy import copy

a, b = map(int, input().split())

'''
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
6 : 110
7 : 111
8 : 1000
1001
1010
1011
1100
1101
1110
1111

10000
10001
10010
10011
10100
10101
10110
10111
11000
_____
1
1 | 2
1 2 | 2 3
1 2 2 3 | 2 3 3 4
1 2 2 3 2 3 3 4 | 2 3 3 4 3 4 4 5
----
accum sum
1 |
2 | 4
5 6 | 8 11
12 14 16 19 | 21 24 27 31
32 33 ... 
sum(2 ** k) = 2 * sum(2 ** (k - 1)) + 2 ** (k -1)
'''

one_cnt = [0 for _ in range(int(log2(b)) + 1)]
one_cnt[0] = None
one_cnt[1] = 1
one_cnt[2] = 1
one_cnt[3] = 2
for k in range(1, int(log2(b)) + 1):
    before_start = 2 ** (k - 1)
    start = 2 ** k
    end = 2 ** (k + 1) - 1
    mid = (start + end) // 2
    '''
    2 : 3 = 1 : 1
    3 : 4 = x+1 -> 2 : 2
    '''
    one_cnt[start : mid + 1] = one_cnt[before_start : start]
    one_cnt[mid + 1 : end + 1] = list(map(lambda x: x+1, one_cnt[start : mid + 1]))
print(sum(one_cnt[a:b + 1]))
