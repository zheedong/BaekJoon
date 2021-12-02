test_case_1 = """
5            # N
4 1 5 2 3
5            # M
1 3 7 9 5
"""
'''
result
1
1
0
0
1
'''

N = int(input())
A = list(map(int, input().split()))

A_set = set(A)        # Set in으로 문제 한 번에 해결...

M = int(input())
B = list(map(int, input().split()))

for i in range(0, M):
    if B[i] in A_set:
        print(1)
    else:
        print(0)