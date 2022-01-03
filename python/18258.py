from collections import deque
import sys

n = int(input())

queue = deque([])

for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    command = temp[0]
    try:
        num = temp[1]
    except:
        num = None
    if command == "push":
        queue.append(num)
    elif command == "pop":
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(1 if not queue else 0)
    elif command == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    elif command == "back":
        try:
            print(queue[-1])
        except:
            print(-1)
    else:
        print("ERROR")
    