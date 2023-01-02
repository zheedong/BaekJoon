'''
            [0 + 1]             [1 + 1]         [1 + 2 + 3] [1 + 2 + 3 + 1]
            [1 + 2]         [1 + 2 + 2]     [1 + 2 + 3 + 2]
        [1 + 2 + 1]     [1 + 2 + 3 + 3] [1 + 2 + 3 + 4 + 3]
    [1 + 2 + 3 + 4] [1 + 2 + 3 + 4 + 2]
[1 + 2 + 3 + 4 + 1]

01 02 06 07 15 16 28 29
03 05 08 14 17 27 30
04 09 13 18 26 31
10 12 19 25 32
11 20 24 33
21 23 34
22 35
36

a/b
sum     range       count
2       01          1 
3       02 ~ 03     2  
4       04 ~ 06     3
5       07 ~ 10     4
6       11 ~ 15     5

x = 0 + 1 + 2 + 3 ... + n + k     (1 <= k <= n + 1)
total = n
part = 1
for _ in range(k - 1):
    part += 1
if n is odd:
    part / (total - part)
else:
    (total - part) / part

'''

def get_n_k(x):
    n = 0
    while True:
        k = x - (n * (n + 1)) // 2
        if k >= 1 and k <= n + 1:
            break
        n += 1
    return n, k


x = int(input())
n, k = get_n_k(x)
if n % 2 == 0:
    print(f"{n + 2 - k}/{k}")
else:
    print(f"{k}/{n + 2 - k}")
