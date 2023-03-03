k = int(input())

'''
4
7 - 2nd

44
47
74
77 - 2 + 4th

444
447
474
477
744
747
774
777 - 2 + 4 + 8 th

7777 - 2 + 4 + 8 + 16 th

'4' * n - 2^(n) - 1 th
'7' * n - 2^(n + 1) - 2 th

k th num
n ++
2 ** n - 1 <= k <= 2 ** (n + 1) - 2
-> k th num은 n 자리 수
'''

n = 1
while True:
    # k 번째 수는 n 자리 수
    if 2 ** n - 1 <= k <= 2 ** (n + 1) - 2:
        break
    else:
        n += 1

# print(f"{k}번째 수는 {n}자리 수")
# print(f"{n - 1}자리 수 중 최대 값은 {'7' * (n - 1)}이고, {2 ** n - 2}번쨰 수")

cur_str = str(bin(k - (2 ** n - 1)))[2:]
res = []
for num in list(cur_str.zfill(n)):
    if num == '0':
        res.append('4')
    else:
        res.append('7')
print("".join(res))

'''
n 자리 수
0 n개 -> 4 n개
0000..0 -> 444444...4 : 2 ** n - 1th
0000..1 -> 444444...7 : 2 ** n - 1 + 1 th
0000...10 -> 444444..74 :
n 자리에서 첫 번째 수는 2 ** n - 1번째
'''
