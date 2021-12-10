import sys

m = int(input())

my_set = set()

one_to_twenty_set = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

for i in range(0, m):
    tmp_inp = sys.stdin.readline().strip().split()
    
    if len(tmp_inp) == 1:
        command = tmp_inp[0]
    else:
        command = tmp_inp[0]
        inp_num = int(tmp_inp[1])

    if command == 'add':
        my_set = my_set | set([inp_num])
    elif command == 'remove':
        my_set = my_set - set([inp_num])
    elif command == 'check':
        if inp_num in my_set:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if inp_num in my_set:
            my_set = my_set - set([inp_num])
        else:
            my_set = my_set | set([inp_num])
    elif command == 'all':
        my_set = my_set | one_to_twenty_set
    elif command == 'empty':
        my_set = my_set & set()