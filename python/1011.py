t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    k = 1
    while True:
        if (y - x) == 1:
            print(1)
            break
        if k ** 2 < (y - x) <= k ** 2 + k:
            '''
            1 < ? <= 2 : 2
            4 < ? <= 6 : 4
            9 < ? <= 12 : 6
            '''
            print(2 * k)
            break
        if k ** 2 + k < (y - x) <= (k + 1) ** 2:
            '''
            2 < ? <= 4 : 3
            6 < ? <= 9 : 5
            '''
            print(2 * k + 1)
            break
        k += 1


'''
1 = 1
1 1 = 2

1 2 1 = 4
1 2 2 1 = 6

1 2 3 2 1 = 9
1 2 3 3 2 1 = 12

1 2 3 4 3 2 1 = 16
1 2 3 4 4 3 2 1 = 20

1 ... n ... 1 = n^2
1 ... n n ... 1 = n^2 + n
'''
