import sys

deque = []

n = int(input())

for i in range(0, n):
    tmp_inp = sys.stdin.readline().strip().split()

    if len(tmp_inp) == 1:
        command = tmp_inp[0]
    else:
        command, num = tmp_inp[0], int(tmp_inp[1])
        
    if command == "push_front":
        deque.insert(0, num)
    elif command == "push_back":
        deque.append(num)
    elif command == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
            deque = deque[1:]
    elif command == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            deque = deque[0:-1]
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif command == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif command == "back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])